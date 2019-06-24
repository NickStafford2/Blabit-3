
/*	for flash message */
  function hideMessageBox() {
      var messageBox = document.getElementById("messageBox");
      while (messageBox.firstChild) {
          messageBox.removeChild(messageBox.firstChild);
      }
      messageBox.classList.add('removeHeight');
  }

//$("#postButton").click(function() {
function setChatLiveStatus(id, is_live) {
	$.post('/chat_setLive', {
		id: id,
		is_live: true
	});
    alert("clicked");
    console.log('button clicked')
}