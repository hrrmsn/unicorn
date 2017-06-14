// Helper function definitions are here.

var backButton = document.getElementById('back-button');
var startButton = document.getElementById('start-button');


// Add event listeners here.

backButton.addEventListener('click', function(e) {
  window.location = 'http://localhost:8000/greeting';
});

startButton.addEventListener('click', function(e) {
  window.location = 'http://localhost:8000/test';
});