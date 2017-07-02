// Variable declarations here.

var checkButton = document.querySelector('button');
var radioButtons = document.querySelectorAll('input');
var unicornTestForm = document.querySelector('form');

var alertMessages = {
  'english': 'Please answer all questions! The unicorns believe in you.',
  'russian': 'Пожалуйста, ответьте на все вопросы! Единороги верят в вас.'
}


// Add event listeners here.

checkButton.addEventListener('click', function(e) {
  var selectedRadioButtonsNumber = 0;
  for (var i = 0, len = radioButtons.length; i < len; i++) {
    if (radioButtons[i].checked) {
      selectedRadioButtonsNumber++;
    }
  }
  if (selectedRadioButtonsNumber < 10) {
    alert(alertMessages[getSelectedLanguage()]);
  } else {
    unicornTestForm.submit();
  }
});
