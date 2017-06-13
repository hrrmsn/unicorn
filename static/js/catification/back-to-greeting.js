// Helper function definitions are here.

var backButton = document.querySelector('button');


// Add event listeners here.

backButton.addEventListener('click', function(e) {
  window.location = 'http://localhost:8000/greeting';
});