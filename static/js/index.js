// Helper function definitions are here.

var radioButtons = document.querySelectorAll('input');
var radioButtonFirst = radioButtons[0];
var radioButtonSecond = radioButtons[1];

var radioButtonsForm = document.querySelector('form');


// Event listeners are here.

radioButtonsForm.addEventListener('submit', function(e) {
  if (!radioButtonFirst.checked && !radioButtonSecond.checked) {
    alert('You should choose at least one language.');
    e.preventDefault();
  }
});
 