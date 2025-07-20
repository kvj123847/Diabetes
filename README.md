# Diabetes Prediction Web App

This is a Flask-based web application for predicting diabetes status using a machine learning model.

## Features

- User-friendly web interface for inputting health data
- Scales input data and predicts diabetes status using a trained model
- Displays prediction results on the same page

## Requirements

- Python 3.x
- Flask
- joblib
- numpy
- Pre-trained model file: `diabetes_model.pkl`
- Pre-trained scaler file: `scaler.pkl`

## Setup

1. Clone or download this repository.
2. Ensure `diabetes_model.pkl` and `scaler.pkl` are present in the project directory.
3. Install dependencies:
   ```
   pip install flask joblib numpy
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

- Enter the required health parameters in the form.
- Submit to get a prediction on diabetes status.

## File Structure

- `app.py` - Main Flask application
- `diabetes_model.pkl` - Trained machine learning model
- `scaler.pkl` - Scaler for input normalization
- `templates/index.html` - Web interface (HTML template)
- `README.md` - Project documentation

## License

This project is for educational purposes.
