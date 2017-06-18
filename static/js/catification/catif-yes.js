// Helper function definitions are here.

var backButton = document.getElementById('back-button');
var startButton = document.getElementById('start-button');


// Add event listeners here.

backButton.addEventListener('click', function(e) {
  var requestUrl = 'http://localhost:8000/greeting';
  var parameters = {'answer': 'greeting', 'language': getSelectedLanguage()};
  sendPostRequest(requestUrl, parameters);
});

startButton.addEventListener('click', function(e) {
  var requestUrl = 'http://localhost:8000/test';
  var parameters = {'answer': 'test', 'language': getSelectedLanguage()};
  sendPostRequest(requestUrl, parameters);
});