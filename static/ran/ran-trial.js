var i = 0;
var ii = 0;
var RanStimuli = document.getElementsByClassName('RANStim');
var outerLoopDurration = 5500;
var recordTrialDuration = outerLoopDurration - 600;
var stimid;
var ding = document.getElementById('ding');
var tone = document.getElementById('tone');
ding.volume = 0.55;
tone.volume = 0.45;


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
    let response = fetch(`/${languageCode}/ran/savetrialdata/`, {
        method: "POST",
        body: data,
        headers: { 
            'stimid': stimid,
            'trialBlock': currentTrialBlock,
            'researchGroup': userRG,
            "X-CSRFToken": csrftoken 
        },
    })
}



function recordTrial(stream) {
    // setTimeout(function() {
        console.log('record trial started, inside timeout f')
        const options = {mimeType: 'audio/webm'};
        var recordedChunks = [];
        var mediaRecorder = new MediaRecorder(stream, options);
        var stimid = RanStimuli[ii].src.slice(-7,-4);

        function clearMediaStream(){
            console.log('media stream cleared')
            stream.getTracks().forEach((track) => {
                track.stop();
            });
        }

        function stopRecording() {
            console.log('stopRecording called')
            setTimeout(function() {
                console.log('stopRecording executed')
                blob = new Blob(recordedChunks, {type: 'audio/wav'});
                console.log(blob)
                sendData(blob, stimid);
                clearMediaStream();

            }, recordTrialDuration)
        }
        mediaRecorder.start(100);
        stopRecording();
        mediaRecorder.addEventListener('dataavailable', function(e) {
            if (e.data.size > 0) {
                console.log('data')
                recordedChunks.push(e.data);
            }
        });
    // }, 500)
}


function hideLast() {
    setTimeout(function() { 
        document.getElementById('nextButtonNotice').style.display = 'block';
    }, outerLoopDurration)
}

function showStim() {
    setTimeout(function(){
        RanStimuli[ii].style.display = 'block';
        console.log(RanStimuli[ii].src.slice(-7,-4))
        navigator.mediaDevices.getUserMedia({ audio: true, video: false })
            .then(recordTrial)
        hideStim();
    }, 500)
}

function hideStim() {
    setTimeout(function(){
        RanStimuli[ii].style.display = 'none';
    }, 500)
}
 
function hideDot() {
    setTimeout(function(){
        document.getElementById('focusDot').style.display = 'none';
    }, 500)
}


function firstTrial() {
    setTimeout(function() {
        for (const child of RanStimuli){
            child.style.display = 'none';
        }
        document.getElementById('focusDot').style.display = 'block';
        ding.play();            
        
        showStim();
        hideDot();
        ii = i
        i++;
        RAN_trialCycle();
    }, 500)
}

function RAN_trialCycle() {
    // var RanStimuli = document.getElementsByClassName('RANStim');
    console.log(RanStimuli)    
    setTimeout(function() {
        for (const child of RanStimuli){
            child.style.display = 'none';
        }
        document.getElementById('focusDot').style.display = 'block';
        ding.play();
        
        showStim();
        hideDot();
        ii = i
        i++;
        console.log(RanStimuli.length)
        if (i < RanStimuli.length) {
            RAN_trialCycle();
        } else {
             hideLast();
        }
    }, outerLoopDurration)
}

function startingIn(){
    document.getElementById('startTrialMessage').style.display = 'none';
    document.getElementById('startingTrialIn').style.display = 'block';
    document.getElementById('startingTrialInThree').style.display = 'block';
    setTimeout(function(){
        console.log('3')
        document.getElementById('startingTrialInThree').style.display = 'none';
        document.getElementById('startingTrialInTwo').style.display = 'block';
    }, 1000);
    setTimeout(function(){
        console.log('2')
        document.getElementById('startingTrialInTwo').style.display = 'none';
        document.getElementById('startingTrialInOne').style.display = 'block';
    }, 2000);
    setTimeout(function(){
        console.log('1')
        document.getElementById('startingTrialIn').style.display = 'none';
        firstTrial();
    }, 3000);
}

window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed'); 
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

});