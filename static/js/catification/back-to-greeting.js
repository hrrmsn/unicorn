// Helper function definitions are here.

var backButton = document.querySelector('button');


// Add event listeners here.

backButton.addEventListener('click', function(e) {
  var requestUrl = 'http://localhost:8000/greeting';
  var parameters = {'answer': 'greeting', 'language': getSelectedLanguage()};
  sendPostRequest(requestUrl, parameters);
});