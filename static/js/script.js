  
$(document).ready(function() {
  $('.open-popup-button').click(function() {
    $('.popup').fadeIn();
    $('.blur-overlay').fadeIn();
  });

  $('.close-popup-button').click(function() {
    $('.popup').fadeOut();
    $('.blur-overlay').fadeOut();
  });
});

function showPredictionForm() {
    document.getElementById('price-prediction-popup').style.display = 'flex';
}

function showRecommendationForm() {
    document.getElementById('prediction-popup').style.display = 'flex';
}

function closePredictionForm() {
    document.getElementById('price-prediction-popup').style.display = 'none';
}

function closeRecommendationForm() {
    document.getElementById('prediction-popup').style.display = 'none';
}

function closePopup() {
        $('#prediction-popup').hide();
        $('#crop-form')[0].reset(); 
        $('#result').text(''); 
        $('#price-prediction-popup').hide();
        $('#price-prediction-form')[0].reset();
        $('#price-result').text('');
    }

  
window.onload = onPageLoad;