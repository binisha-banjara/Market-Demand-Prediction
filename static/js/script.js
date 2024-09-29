  
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

// Show Crop Price Prediction Form
function showPredictionForm() {
    document.getElementById('prediction-popup').style.display = 'flex';
}

// Show Crop Recommendation Form
function showRecommendationForm() {
    document.getElementById('recommendation-popup').style.display = 'flex';
}

// Close Crop Price Prediction Form
function closePredictionForm() {
    document.getElementById('prediction-popup').style.display = 'none';
}

// Close Crop Recommendation Form
function closeRecommendationForm() {
    document.getElementById('recommendation-popup').style.display = 'none';
}

function closePopup() {
        $('#prediction-popup').hide();
        $('#crop-form')[0].reset(); // Resets the form
        $('#result').text(''); // Clears the result text
    }

  
window.onload = onPageLoad;