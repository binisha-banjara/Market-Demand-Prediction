  
$(document).ready(function() {
  // Function to open the popup
  $('.open-popup-button').click(function() {
    $('.popup').fadeIn();
    $('.blur-overlay').fadeIn();
  });

  // Function to close the popup
  $('.close-popup-button').click(function() {
    $('.popup').fadeOut();
    $('.blur-overlay').fadeOut();
  });
});


  
window.onload = onPageLoad;