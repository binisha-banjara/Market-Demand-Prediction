import os
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model from the models directory
model_path = os.path.join("models", "CropRecommender.pkl")
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)


# Define route for the home page
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
            prediction = model.predict([[n, p, k,temperature,humidity, ph, rainfall ]])[0]
            return render_template("index.html", prediction=prediction)

        except Exception as e:
            print(f"An error occurred: {e}")  # Log any other errors
            return render_template(
                "index.html", prediction="An error occurred during prediction."
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
