var i = 0;
var elipsis = document.getElementById('elipsis');
const VidnarStimuli = document.getElementsByClassName("VidnarStimuli");
var loadingMsg = document.getElementById("loadingDataMessage");




function getInterval(vid){
    var vid = vid;
    // console.log(vid.duration)
    if (vid.duration < 30) {
        var postVidinterval = 25;
        document.getElementById('stopRecordingTimeout').innerHTML = " 10 ";
    } else {
        var postVidinterval = 50;
        document.getElementById('stopRecordingTimeout').innerHTML = " 20 ";
    }
    return postVidinterval;
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




function sendData(data, stimid) {
    let csrftoken = getCookie('csrftoken');
    let response = fetch("../../savetrialdata/", {
        method: "POST",
        body: data,
        headers: { 
            'stimid': stimid,
            'trialBlock': currentBlock,
            'researchGroup': userRG,
            "X-CSRFToken": csrftoken 
        },
    })
}




function recordTrial(stream) {
    const options = {mimeType: 'audio/webm'};
    var recordedChunks = [];
    var mediaRecorder = new MediaRecorder(stream, options);
    var stimid = vidnr;
    var currentVid = document.getElementById(`vid_${vidnr}`)
    if (currentVid.duration < 30){
        var PVI = 9500;
    } else {
        var PVI = 19500;
    }
    var srto = (currentVid.duration * 1000) + PVI;




    function clearMediaStream(){
        stream.getTracks().forEach((track) => {
            track.stop();
        });
    }



    
    function stopRecording() {
        setTimeout(function(){
            blob = new Blob(recordedChunks, {type: 'audio/wav'});
            sendData(blob, stimid);
            clearMediaStream();
        }, srto);
    }




    stopRecording();
    mediaRecorder.start(100);
    mediaRecorder.addEventListener('dataavailable', function(e) {
        if (e.data.size > 0) {
            recordedChunks.push(e.data);
        }
    });
}




function hideVid(currentVid){
    var tohide = currentVid;
    setTimeout(function(){
        tohide.style.display = 'none';
        document.getElementById('nextButtonNotice').style.display = 'block';
    }, 250)
}




function move(x) {
    var x = x
    elipsis.style.display = 'block';
    if (i == 0) {
        i = 1;
        var elem = document.getElementById("myBar");
        var width = 0.25;
        var id = setInterval(frame, getInterval(x));
        function frame() {
            if (width >= 100) {
                clearInterval(id);
                i = 0;
                elipsis.style.display = 'none';
                document.getElementById('myProgress').style.display = 'none';
                hideVid(x);
            } else {
                width+=0.25;
                elem.style.width = width + "%";
            }
        }
    }
}




function Trial(){
    var currentVid = document.getElementById(`vid_${vidnr}`)
    navigator.mediaDevices.getUserMedia({ audio: true, video: false })
        .then(recordTrial)
    currentVid.style.display = "block";
    currentVid.volume = 0.2;
    currentVid.play();
    setTimeout(function(){
        move(currentVid);
        document.getElementById('myProgress').style.display = 'block';
    }, currentVid.duration * 1000)
}




function startingIn(){
    document.getElementById('startTrialMessage').style.display = 'none';
    document.getElementById('startingTrialIn').style.display = 'block';
    document.getElementById('startingTrialInThree').style.display = 'block';
    setTimeout(function(){
        document.getElementById('startingTrialInThree').style.display = 'none';
        document.getElementById('startingTrialInTwo').style.display = 'block';
    }, 1000);
    setTimeout(function(){
        document.getElementById('startingTrialInTwo').style.display = 'none';
        document.getElementById('startingTrialInOne').style.display = 'block';
    }, 2000);
    setTimeout(function(){
        document.getElementById('startingTrialIn').style.display = 'none';
        Trial();
    }, 3000);
}




window.onload = function(){

    document.getElementById('startTrialButton').addEventListener('click', function(){
        startingIn();
    })

    navigator.mediaDevices.getUserMedia({ audio: true, video: false })
        .then(function(stream) {
            document.getElementById('startTrialButton').style.display = 'block';
            stream.getTracks().forEach((track) => {
                track.stop();
            })
        });
    const vid = document.getElementById(`vid_${vidnr}`);
    console.log('vid', vid); // do you see this?
    vid.oncanplaythrough = () => {
        // console.log("VERT DE FEERERRRRRRKKKK!");
        loadingMsg.style.display = "none";
        document.getElementById("startTrialMessage").style.display = "block";
    }
    // For whatever reason that I can't figure out, if the user reloads the page using
    // the browser buttons, ctrl+r, or ctrl+shift+R, the event won't fire a second time.
    // I [RB] suck at javascript, so if someone wants to rewrite this, please (!) please do.
};