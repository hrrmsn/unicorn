// Helper function definitions are here.

var languageLabelTextContent = document.querySelector('label').textContent;

var selectLanguage = document.querySelector('select');
var englishSelectOption = selectLanguage[0];
var russianSelectOption = selectLanguage[1];
var selectedLanguage;

var wsgiFunctionName = document.querySelector('wsgi-function').textContent;


// Add event listeners here.

window.addEventListener('load', function(e) {
  if (languageLabelTextContent === 'language:') {
    englishSelectOption.selected = true;
    selectedLanguage = 'eng';
  } else {
    russianSelectOption.selected = true;
    selectedLanguage = 'rus';
  }
});

selectLanguage.addEventListener('change', function(e) {
  var xhttp = new XMLHttpRequest();
  xhttp.open('POST', wsgiFunctionName + '?lang=' + selectedLanguage, true);
  xhttp.send();
  console.log('ajax request was sent');
});

