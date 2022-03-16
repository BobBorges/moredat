var stimDivs = document.getElementsByClassName("stimDiv");
console.log(stimDivs.length);
console.log(`NEXT : ${NEXT}`)

var trialStart;
var trialClick;

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



var stimDivCounter = 0;
var replayCounter = 0;
function Trial(){
	document.getElementById('startDiv').style.display = 'none';
	document.getElementById('dotDiv').style.display = 'block';
	document.getElementById('replayButtonDiv').style.display = 'block';
	trialStart = Date.now()
	setTimeout(function(){
		document.getElementById('dotDiv').style.display = 'none';
		document.getElementById(`stimDiv_${stimDivCounter}`).style.display = 'block';
		document.getElementById(`audiostim_${stimDivCounter}`).play();
	}, 1000);

}

function incrementReplay() {
	console.log("REPLAY");
	replayCounter++;
	document.getElementById(`audiostim_${stimDivCounter}`).play();
}

function select(location, stim){
	const trialClick = Date.now();
	const xhttp = new XMLHttpRequest();
	const data = new FormData();
	xhttp.onload = function(){
		console.log(this.responseText);
		if (this.responseText === "OK"){
			console.log("data sent");
		} else {
			console.log("fuck")
		}
	}

	let csrftoken = getCookie('csrftoken');
	xhttp.open("POST", "../../savedata/")
	data.append('csrfmiddlewaretoken', csrftoken);
	data.append('clicked_quad', `${location}`);
	data.append('clicked_stim', `${stim}`);
	data.append('replays', `${replayCounter}`);
	data.append('renderTime', `${trialStart}`);
	data.append('clickTime', `${trialClick}`);
	xhttp.send(data);

	document.getElementById(`stimDiv_${stimDivCounter}`).style.display = "none"

	console.log(`stim counter1: ${stimDivCounter}`);
	stimDivCounter++;
	console.log(`stim counter2: ${stimDivCounter}`);

	console.log(`Replay Audio Counter: ${replayCounter}`)
	replayCounter = 0;

	if (stimDivCounter > stimDivs.length - 1) {
		console.log('all stims done');
		window.location.href = NEXT;
	} else {
		console.log('more stims...');
		Trial();
	}
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
        Trial();
    }, 3000);
}



window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed'); 
    document.getElementById('startTrialButton').addEventListener('click', function(){
        startingIn();
    })
});
