var writtenResponseDiv = document.getElementById('div_id_written_response');
var commentaryDiv = document.getElementById('div_id_commentary');
var responseType = document.getElementById('id_response_type');
var recorderDiv = document.getElementById('wltrecorderdiv');


let shouldStop = false;
let shouldStart = false;
let stopped = true;
const downloadLink = document.getElementById('download');
const stopButton = document.getElementById('stop');
const startButton = document.getElementById('start');
const player = document.getElementById('player');
const submitButton = document.getElementById('wltSubmitButton');
var mediaRecorder;


function createFileList(a) {
  a = [].slice.call(Array.isArray(a) ? a : arguments)
  for (var c, b = c = a.length, d = !0; b-- && d;) d = a[b] instanceof File
  if (!d) throw new TypeError('expected argument to FileList is File or array of File objects')
  for (b = (new ClipboardEvent('')).clipboardData || new DataTransfer; c--;) b.items.add(a[c])
  return b.files
}


function insertAfter(referenceNode, newNode) {
  referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}


function getCookie(name) {
    var cookieValue = null;
  	if (document.cookie && document.cookie !== '') {
      	var cookies = document.cookie.split(';');
      	for (var i = 0; i < cookies.length; i++) {
          	var cookie = cookies[i].trim();
          	// Does this cookie string begin with the name we want?
          	if (cookie.substring(0, name.length + 1) === (name + '=')) {
             	cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              	break;
          	}
      	}
  	}
  	return cookieValue;
}


function sendData(data) {
    let csrftoken = getCookie('csrftoken');
  	let response = fetch("../../savespndata", {
 			method: "POST",
  		body: data,
  		headers: { "X-CSRFToken": csrftoken },
  	})
 	}

document.addEventListener("DOMContentLoaded", function(event) { 
    writtenResponseDiv.style.display = 'none';
    commentaryDiv.style.display = 'none';
    recorderDiv.style.display = 'none';
});


responseType.addEventListener('change', function(){
	var resp = responseType.value;
	if (resp == 'Record response') {
    	writtenResponseDiv.style.display = 'block';
    	commentaryDiv.style.display = 'block';
    	recorderDiv.style.display = 'block';
	} else {
	    writtenResponseDiv.style.display = 'none';
    	commentaryDiv.style.display = 'block';
    	recorderDiv.style.display = 'none';
	}
})




var recordedChunks = [];
const handleSuccess = function(stream) {
	const options = {mimeType: 'audio/webm'};
	var mediaRecorder = new MediaRecorder(stream, options);


	function clearMediaStream(){
		stream.getTracks().forEach((track) => {
			track.stop();
		});
	}


	if(shouldStart === true && stopped === true) {
		recordedChunks = [];
		mediaRecorder.start(250);
		stopped = false;
		shouldStart = false;
	}
	

	if(stopped === true){
		clearMediaStream();
	}


	stopButton.addEventListener('click', function() {
		shouldStop = true;
		clearMediaStream();
		stopped = true;
	});


	mediaRecorder.addEventListener('dataavailable', function(e) {
		if (e.data.size > 0) {
			recordedChunks.push(e.data);
		}
	});


	mediaRecorder.addEventListener('stop', function() {
		var blob = new Blob(recordedChunks, {type:'audio/wav'})
		var nFile = new File([blob], 'newfile.wav', {type:'audio/wav'})
		var input = document.createElement('input')
		input.type = 'file';
		input.files = createFileList(nFile);
		input.name = 'hidden_field';
		input.style.display = 'none';
		document.getElementById('THEFORM').appendChild(input);

		downloadLink.href = URL.createObjectURL(blob);
		player.src = downloadLink
		
	});


	startButton.addEventListener('click', function() { 
		shouldStart = true;
		shouldStop = false;
		stopped = true;
		navigator.mediaDevices.getUserMedia({ audio: true, video: false })
			.then(handleSuccess);
	});
};


navigator.mediaDevices.getUserMedia({ audio: true, video: false })
	.then(handleSuccess);