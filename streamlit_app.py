# prompt: Crea un código para una web con streamlit que permita usar el modelo .joblib anterior y permita al usuario introducir los datos necesarios de una estrella (dando un rango de valores de ejemplo) y predecir cual es su clasificación indicando sus características entre las cuales debe aparecer su color. También debe devolver una imagen del tipo de estrella.

import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load('stars_model.joblib')

# Function to predict star type
def predict_star_type(temperature, luminosity, radius, magnitude):
    # Create a DataFrame with input features
    input_data = pd.DataFrame({
        'Temperature': [temperature],
        'L': [luminosity],
        'R': [radius],
        'A_M': [magnitude]
    })

    # Predict the star type
    prediction = model.predict(input_data)

    # Map the numeric prediction back to star types
    star_types = {0: 'M', 1: 'A', 2: 'B', 3: 'F', 4: 'O', 5: 'K', 6: 'G'}
    predicted_star_type = star_types.get(prediction[0], "Unknown")

    return predicted_star_type

# Streamlit app
st.title("Clasificador de tipos de estrella")
st.write('Aplicación de clasificación de estrellas')
st.image("img/fondo-estrellas.jpg", use_container_width=True)

# Input features
temperature = st.number_input("Temperature (K)", min_value=2000, max_value=40000, value=5778, step=100)
luminosity = st.number_input("Luminosity (L/Lo)", min_value=1, max_value=1000000, value=1, step=1)
radius = st.number_input("Radius (R/Ro)", min_value=1, max_value=2000, value=1, step=1)
magnitude = st.number_input("Absolute Magnitude (Mv)", min_value=-10, max_value=20, value=5, step=1)

# Prediction button
if st.button("Predict"):
    predicted_type = predict_star_type(temperature, luminosity, radius, magnitude)

    # Display the prediction and image
    st.write(f"Predicted Star Type: {predicted_type}")

    # Add images according to the predicted type
    # Load placeholder image
    placeholder_image = st.image("img/fondo-estrellas.jpg")

    # Determine image based on star type
    if predicted_type == 'M':
        placeholder_image = st.image("img/m_star_image.jpg")
    elif predicted_type == 'A':
        placeholder_image = st.image("img/a_star_image.jpg")
    elif predicted_type == 'B':
        placeholder_image = st.image("img/b_star_image.jpg")
    else:
        star_image = placeholder_image # Default to placeholder if no image found


    st.image(star_image, caption=f'Image of a {predicted_type} star', use_column_width=True)