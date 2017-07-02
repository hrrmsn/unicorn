// Variable declarations are here.

var passTestAgainLink = document.getElementById('pass-test-again');
var notifyUnicornsButton = document.querySelector('button');

var thankYouAlertMessages = {
  'english': 'Thank you! The unicorns will be informed.',
  'russian': 'Спасибо! Единороги будут проинформированы.'
};

var alreadyInformedAlertMessages = {
  'english': 'The unicorns are already informed!',
  'russian': 'Мы уже проинформировали единорогов!'
};

var score = document.querySelector('score');
var scoreValue = parseInt(score.textContent);

var elementsToHide = document.getElementsByClassName('hide-if-bad-result');


// Add event listeners here.

window.addEventListener('load', function(e) {
  if (scoreValue < 8) {
    for (var i = 0, len = elementsToHide.length; i < len; i++) {
      elementsToHide[i].style.display = 'none';
    }
  }
});

if (passTestAgainLink) {
  passTestAgainLink.addEventListener('click', function(e) {
    e.preventDefault();

    var requestUrl = mainUrl + 'test';
    var parameters = {'answer': 'test', 'language': getSelectedLanguage()};
    sendPostRequest(requestUrl, parameters);
  });
}

if (notifyUnicornsButton) {
  notifyUnicornsButton.addEventListener('click', function(e) {
    var xhttp = new XMLHttpRequest();
    var haveUnicornsBeenInformed = '';
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        haveUnicornsBeenInformed = this.responseText;

        if (haveUnicornsBeenInformed === 'True') {
          alert(alreadyInformedAlertMessages[getSelectedLanguage()]);
        } else {
          var xhttpLocal = new XMLHttpRequest();
          xhttpLocal.open('POST', '/notify', true);
          xhttpLocal.send();
          alert(thankYouAlertMessages[getSelectedLanguage()]);
        }
      }
    }
    xhttp.open('POST', '/is-already-informed', true);
    xhttp.send();
  });  
}
