// Variable definitions are here.

var languageLabelTextContent = document.querySelector('label').textContent;

var selectLanguage = document.querySelector('select');
var englishSelectOption = selectLanguage[0];
var russianSelectOption = selectLanguage[1];

var wsgiFunctionName = document.querySelector('wsgi-function').textContent;

var mainUrl = 'http://localhost:8000/';


// Helper function definitions are here.

function sendPostRequest(requestUrl, parameters) {
  var form = document.createElement('form');
  form.setAttribute('method', 'post');
  form.setAttribute('action', requestUrl);

  for (var property in parameters) {
    if (parameters.hasOwnProperty(property)) {
      var inputField = document.createElement('input');
      inputField.setAttribute('type', 'hidden');
      inputField.setAttribute('name', property);
      inputField.setAttribute('value', parameters[property]);

      form.appendChild(inputField);
    }
  }

  document.body.appendChild(form);
  form.submit();
}

function getSelectedLanguage() {
  if (languageLabelTextContent === 'language:') {
    return 'english';
  }
  return 'russian';
}


// Add event listeners here.

window.addEventListener('load', function(e) {
  if (languageLabelTextContent === 'language:') {
    englishSelectOption.selected = true;
  } else {
    russianSelectOption.selected = true;
  }
});

selectLanguage.addEventListener('change', function(e) {
  var selectedLanguage = 'russian';
  if (e.target.value === 'english') {
    selectedLanguage = 'english';
  }
  
  var parameters = {'answer': wsgiFunctionName, 'language': selectedLanguage};
  if (wsgiFunctionName === 'result') {
    parameters['score'] = document.querySelector('score').textContent;
  }

  var requestUrl = mainUrl + wsgiFunctionName;
  if (wsgiFunctionName.substring(0, 5) === 'catif') {
    requestUrl = mainUrl + 'catification';
  }
  sendPostRequest(requestUrl, parameters);
});
