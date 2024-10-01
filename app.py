import os
from flask import Flask, render_template, request, jsonify
import pickle
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model from the models directory
model_path = os.path.join("models", "CropRecommender.pkl")
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

prediction_model_path = os.path.join("models", "market_demand_model.h5")
prediction_model = load_model(prediction_model_path)

dtr = pickle.load(open("dtr.pkl", "rb"))
preprocessor = pickle.load(open("preprocessor.pkl", "rb"))

# Load the list of commodity names
with open("commodity_names.txt", "r") as f:
    commodity_names = [line.strip() for line in f]



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            n = float(request.form.get("n"))
            p = float(request.form.get("p"))
            k = float(request.form.get("k"))
            temperature = float(request.form.get("temperature"))
            humidity = float(request.form.get("humidity"))
            ph = float(request.form.get("ph"))
            rainfall = float(request.form.get("rainfall"))

            # Make prediction
            prediction = model.predict(
                [[n, p, k, temperature, humidity, ph, rainfall]]
            )[0]
            return jsonify({"prediction": prediction})
        except Exception as e:
            print(f"An error occurred: {e}")  # Log any other errors
            return jsonify({"error": "An error occurred during prediction."}), 400

    return render_template("home.html")

@app.route("/get_commodities", methods=["GET"])
def get_commodities():
    return jsonify({"commodities": [name.split("_")[1] for name in commodity_names]})


@app.route("/predict_price", methods=["POST"])
def predict_price():
    if request.method == "POST":
        data = request.json
        date = pd.to_datetime(data["date"])
        commodity = data["commodity"]

        Temperature = data["Temperature"]
        Rainfall = data["Rainfall"]
        Humidity = data["Humidity"]


        Day, Month, Year = date.day, date.month, date.year

        features = np.array(
            [
                [
                    commodity,
                    Year,
                    Month,
                    Day,
                    Temperature,
                    Rainfall,
                    Humidity,
                ]
            ],
            dtype=object,
        )
        transformed_features = preprocessor.transform(features)

        predicted_price = dtr.predict(transformed_features).reshape(1, -1)

        # print(predicted_price)
        # print(type(predicted_price))
        predicted_price = str(predicted_price[0][0])

        print(predicted_price)
        print(type(predicted_price))

        return jsonify({"predicted_price": predicted_price})
    return render_template("home.html")

    # # Prepare input data
    # input_data = pd.DataFrame(
    #     {"year": [date.year], "month": [date.month], "day_of_year": [date.day]}
    # )

    # # One-hot encode the commodity
    # for commodity in commodity_names:
    #     input_data[commodity] = (
    #         1 if commodity == f"Commodity_{selected_commodity}" else 0
    #     )

    # # Reshape for LSTM input (assuming 1 time step)
    # input_reshaped = input_data.values.reshape((1, 3, input_data.shape[1]))

    # # Make prediction
    # predicted_price = prediction_model.predict(input_reshaped)[0][0]

    # return jsonify({"predicted_price": float(predicted_price)})


if __name__ == "__main__":
    app.run(debug=True)
