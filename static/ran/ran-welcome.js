function showHideDetails() {
    var linkShow = document.getElementById('deetsAshow');
    var linkHide = document.getElementById('deetsAhide');
    var details = document.getElementById('experimentDetails');

    if(details.style.display === 'none') {
        linkShow.style.display = 'none';
        linkHide.style.display = 'inline';
        details.style.display = 'block';
    } else {
        linkShow.style.display = 'inline';
        linkHide.style.display = 'none';
        details.style.display = 'none';
    }
}

var testaudiolink = document.getElementById('testAudioButton');
var GObutton = document.getElementById('getGoingButton');

testaudiolink.addEventListener('click', (event) => {
    GObutton.disabled = false;
});