// Helper function definitions are here.

var radioButtons = document.querySelectorAll('input');
var radioButtonsForm = document.querySelector('form');
var submitButton = document.querySelector('button');

alertMessages = {
  'send': 'You should choose an answer. Make up your mind!',
  'клик': 'Необходимо что-нибудь выбрать. Решайтесь!'
}


// Event listeners are here.

radioButtonsForm.addEventListener('submit', function(e) {
  for (var i = 0, len = radioButtons.length; i < len; i++) {
    if (radioButtons[i].checked) {
      return;
    }
  }
  buttonText = submitButton.textContent || submitButton.innerText;
  alert(alertMessages[buttonText]);
  e.preventDefault();
});
 