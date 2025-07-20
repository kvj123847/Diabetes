from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        data = [float(x) for x in request.form.values()]
        final_input = np.array(data).reshape(1, -1)
        final_scaled = scaler.transform(final_input)

        # Predict
        prediction = model.predict(final_scaled)[0]
        # Use threshold to determine diabetes status
        if prediction > 140:
            result = "The person has diabetes."
        else:
            result = "The person does not have diabetes."

        return render_template('index.html', prediction_text=result)
    except:
        return render_template('index.html', prediction_text="Invalid input. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
