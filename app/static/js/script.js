
/*	for flash message */
  function hideMessageBox() {
      var messageBox = document.getElementById("messageBox");
      while (messageBox.firstChild) {
          messageBox.removeChild(messageBox.firstChild);
      }
      messageBox.classList.add('removeHeight');
  }