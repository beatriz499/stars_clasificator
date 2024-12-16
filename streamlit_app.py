# prompt: Crea un código para una web con streamlit que permita usar el modelo .joblib anterior y permita al usuario introducir los datos necesarios de una estrella y predecir cual es su clasificación.

import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load('stars_model.joblib')

# Title of the app
st.title("Star Classification")

# Input features
temp = st.number_input("Temperature (K)", min_value=0)
luminosity = st.number_input("Luminosity (L/Lo)", min_value=0.0)
radius = st.number_input("Radius (R/Ro)", min_value=0.0)
magnitude = st.number_input("Absolute Magnitude (Mv)", min_value=-10.0, max_value=20.0)

# Create a button to trigger prediction
if st.button("Predict Star Type"):
    # Create a dataframe for the input features
    input_data = pd.DataFrame({
        'Temperature (K)': [temp],
        'Luminosity (L/Lo)': [luminosity],
        'Radius (R/Ro)': [radius],
        'Absolute magnitude (Mv)': [magnitude]
    })
    
    # Make prediction using the loaded model
    prediction = model.predict(input_data)

    # Map numerical prediction to star spectral class
    spectral_class_mapping = {0:'M', 1:'A', 2:'B', 3:'F', 4:'O', 5:'K', 6:'G'}
    predicted_class = spectral_class_mapping.get(prediction[0], "Unknown")

    # Display the prediction
    st.write(f"Predicted Spectral Class: {predicted_class}")