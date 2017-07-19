// Variable definitions are here.

var radioButtons = document.querySelectorAll('input');
var radioButtonFirst = radioButtons[0];
var radioButtonSecond = radioButtons[1];

var radioButtonsForm = document.querySelector('form');

var submitButton = document.querySelector('button');

var alertMessages = {
  'click': 'You should choose a language.',
  'клик': 'Необходимо выбрать какой-нибудь язык.'
}


// Event listeners are here.

radioButtonsForm.addEventListener('submit', function(e) {
  if (!radioButtonFirst.checked && !radioButtonSecond.checked) {
    buttonText = submitButton.textContent || submitButton.innerText;
    alert(alertMessages[buttonText]);
    e.preventDefault();
  }
});
 