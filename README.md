# Market Demand Prediction and Crop Recommendation

## Introduction
This project is focused on predicting market demand for vegetables and providing crop recommendations based on environmental and soil factors. The demand prediction leverages time series forecasting using LSTM (Long Short-Term Memory) models, while the crop recommendation system suggests suitable crops based on soil NPK, temperature, rainfall, and humidity.


## Goals
- **Market Demand Prediction**: To accurately forecast future vegetable prices based on historical data and exogenous weather factors.
- **Crop Recommendation**: To recommend the best crops to plant, based on environmental conditions such as soil nutrients and weather parameters.


## Contributors
- **Binisha Banjara**

## Project Architecture
- **Data Collection**: Historical vegetable price data and weather data from Nepal.
- **Preprocessing**: Handling missing values, feature engineering using rolling means, exponential weighted averages, and one-hot encoding.
- **Modeling**: Using LSTM for time series forecasting of prices and a machine learning model for crop recommendation based on NPK and weather factors.
- **Deployment**: Flask-based web app for user interaction, allowing users to predict prices or get crop recommendations based on inputs.


## Known Issue
- Model accuracy for certain commodities can be improved.
- Need to include external factors as well for the price



# Usage
## Installation


#### Creating Virtual Environment

This package is built using `python-3.8`. 
We recommend creating a virtual environment and using a matching version to ensure compatibility.

```bash
    python3 -m venv venv
    source venv/bin/activate
```

Installing Dependencies

To install the required dependencies, use pip to install them from requirements.txt.

```bash
    pip install -r requirements.txt
```


## Usage Instructions
1. Clone the repository.

2. Install all dependencies as per the above steps.

3. To run the market demand prediction or crop recommendation model, use the Flask app:
```bash
    python app.py
```

# Data Source

- **Price Data**: Historical vegetable prices from the Kalimati market dataset.
  
- **Weather Data**: Historical weather data for Nepal from external sources.


## Code Structure
**src/**: Contains the Flask application code.

**models/**: Trained LSTM models and crop recommendation models.

**dataset/**: Includes the historical datasets used for model training.

## Artifacts Location
**Trained Models**: Stored in models/.

**Dataset**: Stored in data/ as CSV files.

# Results
## Metrics Used

**Crop Price Prediction**: RMSE for evaluating the LSTM model.

**Crop Recommendation**: Accuracy, Precision, Recall, and F1-score for classification of crops.

## Evaluation Results
-The LSTM model achieved an RMSE of 12.28 for vegetable price prediction.

-The crop recommendation model showed an accuracy of 98%.

## Screenshot
![image](https://github.com/user-attachments/assets/0a8773f2-58f9-4b3c-93cd-e8295ac7fd6e)
