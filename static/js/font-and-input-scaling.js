// Variable declarations are here.

var radioButtons = document.getElementsByTagName('input');


// Helpful functions declaration.

function isFirefox() {
  return typeof InstallTrigger !== 'undefined';
}

function setWebkitTransformToElements(elements, value) {
  for (var i = 0, len = elements.length; i < len; i++) {
    elements[i].style.webkitTransform = value;
  }
}

function setFontSizeToElements(elements, fontSize) {
  for (var i = 0, len = elements.length; i < len; i++) {
    elements[i].style.fontSize = fontSize;
  }  
}

function setFontSizeByClassName(className, fontSize) {
  var classElements = document.getElementsByClassName(className);
  setFontSizeToElements(classElements, fontSize);
}

function setFontSizeByTagName(tagName, fontSize) {
  var elements = document.getElementsByTagName(tagName);
  setFontSizeToElements(elements, fontSize);
}


// Add event listeners here.

window.addEventListener('load', function(e) {
  if (isFirefox() === true) {
    setFontSizeByClassName('option', '.9em');
    setFontSizeByClassName('box', '.96em');
    setFontSizeByTagName('button', '.9em');
    setFontSizeByClassName('footer', '.85em');
    setWebkitTransformToElements(radioButtons, 'scale(0.65, 0.65)');
  } else {
    setFontSizeByClassName('option', '.95em');
    setFontSizeByClassName('box', '1.1em');
    setFontSizeByTagName('button', '.8em');
    setFontSizeByClassName('footer', '1em');
    setWebkitTransformToElements(radioButtons, 'scale(0.9, 0.9)');
  }
});