// Variable declarations are here.

var passTestAgainLink = document.getElementById('pass-test-again');


// Add event listeners here.

passTestAgainLink.addEventListener('click', function(e) {
  e.preventDefault();

  var requestUrl = 'http://localhost:8000/test';
  var parameters = {'answer': 'test', 'language': getSelectedLanguage()};
  sendPostRequest(requestUrl, parameters);
});