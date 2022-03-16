	let shouldStop = false;
	let shouldStart = false;
	let stopped = true;
	const downloadLink = document.getElementById('download');
	const stopButton = document.getElementById('stop');
	const startButton = document.getElementById('start');
	const player = document.getElementById('player');
	var mediaRecorder;


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
    	let response = fetch("voice_request/", {
   			method: "POST",
    		body: data,
    		headers: { "X-CSRFToken": csrftoken },
    	})
   	}


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
			blob = new Blob(recordedChunks, {type:'audio/wav'})
			// sendData(blob)
			downloadLink.href = URL.createObjectURL(blob);
			// downloadLink.download = 'acetest.wav';
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
