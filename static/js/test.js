// Variable declarations here.

var checkButton = document.querySelector('button');

var radioButtons = document.querySelectorAll('input');

var alertMessages = {
  'english': 'Please answer all questions! The unicorns believe in you.',
  'russian': 'Пожалуйста, ответьте на все вопросы! Единороги верят в вас.'
}

// Helpful function definitions are here.


// Add event listeners here.
checkButton.addEventListener('click', function(e) {
  var counter = 0;
  for (var i = 0, len = radioButtons.length; i < len; i++) {
    if (radioButtons[i].checked) {
      counter++;
    }
  }
  if (counter < 10) {
    alert(alertMessages[getSelectedLanguage()]);
  }
});