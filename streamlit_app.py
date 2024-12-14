import streamlit as st
import joblib
import pandas as pd

st.title("Clasificador de estrellas")
st.write('Aplicación de clasificación de estrellas')

# # Carga el modelo entrenado
model = joblib.load('stars_model.joblib')

# Input fields for star characteristics
temperature = st.number_input("Temperature (K)", min_value=0)
luminosity = st.number_input("Luminosity (L/Lo)", min_value=0.0)
radius = st.number_input("Radius (R/Ro)", min_value=0.0)
absolute_magnitude = st.number_input("Absolute Magnitude (Mv)", min_value=-10.0, max_value=20.0)

# Create a button to trigger prediction
if st.button("Classify Star"):
    # Create a DataFrame from user input
    input_data = pd.DataFrame({
        'Temperature (K)': [temperature],
        'Luminosity (L/Lo)': [luminosity],
        'Radius (R/Ro)': [radius],
        'Absolute magnitude (Mv)': [absolute_magnitude]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display the prediction
    if prediction == 0:
        st.write("Predicted Spectral Class: M")
    elif prediction == 1:
        st.write("Predicted Spectral Class: A, B, F, O, K, or G")
    else:
        st.write("Prediction error")