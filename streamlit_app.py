# prompt: Crea un código para una web con streamlit que permita usar el modelo .joblib anterior y permita al usuario introducir los datos necesarios de una estrella (dando un rango de valores de ejemplo) y predecir cual es su clasificación indicando sus características entre las cuales debe aparecer su color. También debe devolver una imagen del tipo de estrella.

import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load('stars_model.joblib')

# Define a function to predict the star type
def predict_star_type(data):
    prediction = model.predict(data)
    return prediction[0]


# Streamlit app
st.title("Star Classifier")
st.write('Aplicación de clasificación de mascotas')
st.image("fondo-estrellas.jpg", use_container_width=True)

# Input features
st.sidebar.header("Star Features")
temperature = st.sidebar.number_input("Temperature (K)", min_value=2000, max_value=40000, value=5778, step=100)
luminosity = st.sidebar.number_input("Luminosity (L/Lo)", min_value=0.001, max_value=1000000, value=1.0, step=0.1)
radius = st.sidebar.number_input("Radius (R/Ro)", min_value=0.01, max_value=2000, value=1.0, step=0.1)
absolute_magnitude = st.sidebar.number_input("Absolute Magnitude (Mv)", min_value=-10.0, max_value=20.0, value=5.0, step=0.1)

star_color_options = ['Blue', 'Blue-White', 'Blue White', 'White', 'White-Yellow', 'Yellowish', 'Yellowish-White', 'Yellow', 'Orange', 'Orange-Red', 'Red']
star_color = st.sidebar.selectbox("Star Color", star_color_options)

star_category_options = ['Brown Dwarf', 'Red Dwarf', 'White Dwarf', 'Main Sequence', 'Supergiant', 'Hypergiant']
star_category = st.sidebar.selectbox("Star Category", star_category_options)

# Create a DataFrame from the input features
input_data = pd.DataFrame({
    'Temperature': [temperature],
    'L': [luminosity],
    'R': [radius],
    'A_M': [absolute_magnitude],
    'Star color_' + star_color : [1] ,
    'Star category_' + star_category: [1]
})


# Add columns for other star colors with 0 value
for color in star_color_options:
    if 'Star color_' + color not in input_data.columns:
        input_data['Star color_' + color] = 0
# Add columns for other star category with 0 value
for category in star_category_options:
    if 'Star category_' + category not in input_data.columns:
        input_data['Star category_' + category] = 0


input_data = input_data.reindex(sorted(input_data.columns), axis=1)


# Make the prediction
if st.button("Predict"):
    try:
        spectral_class = predict_star_type(input_data)
        st.write(f"Predicted Spectral Class: {spectral_class}")

        # Display star characteristics (including color)
        st.write("Star Characteristics:")
        st.write(f"  Color: {star_color}")
        st.write(f"  Category: {star_category}")

        # Display corresponding image (replace with your actual image paths)
        if spectral_class == 0:
            st.image("m_star_image.jpg", caption="M Star", use_column_width=True) #Replace m_star_image.jpg
        elif spectral_class == 1:
            st.image("a_star_image.jpg", caption="A Star", use_column_width=True) #Replace a_star_image.jpg
        elif spectral_class == 2:
            st.image("b_star_image.jpg", caption="B Star", use_column_width=True) #Replace b_star_image.jpg
        elif spectral_class == 3:
            st.image("f_star_image.jpg", caption="F Star", use_column_width=True) #Replace f_star_image.jpg
        elif spectral_class == 4:
            st.image("o_star_image.jpg", caption="O Star", use_column_width=True) #Replace o_star_image.jpg
        elif spectral_class == 5:
            st.image("k_star_image.jpg", caption="K Star", use_column_width=True) #Replace k_star_image.jpg
        elif spectral_class == 6:
            st.image("g_star_image.jpg", caption="G Star", use_column_width=True) #Replace g_star_image.jpg

    except Exception as e:
        st.error(f"An error occurred: {e}")