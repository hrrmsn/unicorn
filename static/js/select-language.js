// Helper function definitions are here.

var languageLabelTextContent = document.querySelector('label').textContent;

var selectLanguage = document.querySelector('select');
var englishSelectOption = selectLanguage[0];
var russianSelectOption = selectLanguage[1];

var wsgiFunctionName = document.querySelector('wsgi-function').textContent;


// Add event listeners here.

window.addEventListener('load', function(e) {
  if (languageLabelTextContent === 'language:') {
    englishSelectOption.selected = true;
  } else {
    russianSelectOption.selected = true;
  }
});

selectLanguage.addEventListener('change', function(e) {
  var selectedLanguage = 'eng';
  if (e.target.value === 'russian') {
    selectedLanguage = 'rus';
  }
  window.location = "http://localhost:8000/" + wsgiFunctionName + '?lang=' + selectedLanguage;
});
