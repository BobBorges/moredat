var testaudiolink = document.getElementById('testAudioButton');
var GObutton = document.getElementById('getGoingButton');

testaudiolink.addEventListener('click', (event) => {
    GObutton.disabled = false;
});