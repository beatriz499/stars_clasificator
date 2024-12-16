import streamlit as st
import numpy as np
from joblib import load

# Cargar el modelo
model_path = 'stars_model.joblib'  # Asegúrate de que el archivo esté en la misma ruta o especifica la correcta
model = load(model_path)

# Configurar la página de Streamlit
st.title("Clasificador de Estrellas")
st.write("Introduce los parámetros de tu estrella para predecir su tipo.")
st.image("img/fondo-estrellas.jpg", use_container_width=True)

# Crear entradas para el usuario
temperature = st.number_input("Temperatura (K):", min_value=0.0, value=5000.0, step=100.0)
luminosity = st.number_input("Luminosidad (L/Lo):", min_value=0.0, value=1.0, step=0.1)
radius = st.number_input("Radio (R/Ro):", min_value=0.0, value=1.0, step=0.1)
absolute_magnitude = st.number_input("Magnitud Absoluta (Mv):", value=5.0, step=0.1)

# Selección de características categóricas
star_color = st.selectbox(
    "Color de la Estrella:",
    [
        "Blue", "Blue-White", "Orange", "Orange-Red", "Pale-Yellow-Orange",
        "Red", "White", "White-Yellow", "Whitish", "Yellow-White",
        "Yellowish", "Yellowish-White"
    ]
)

star_category = st.selectbox(
    "Categoría de la Estrella:",
    [
        "Brown Dwarf", "Hypergiant", "Main Sequence", "Red Dwarf", "Supergiant", "White Dwarf"
    ]
)

# Crear un vector de entrada con valores iniciales en 0
input_data = np.zeros(23)

# Asignar valores a las características físicas
input_data[0] = temperature
input_data[1] = luminosity
input_data[2] = radius
input_data[3] = absolute_magnitude

# Mapear el color de la estrella a la posición correspondiente
color_features = [
    "Star color_Blue", "Star color_Blue-White", "Star color_Orange",
    "Star color_Orange-Red", "Star color_Pale-Yellow-Orange", "Star color_Red",
    "Star color_White", "Star color_White-Yellow", "Star color_Whitish",
    "Star color_Yellow-White", "Star color_Yellowish", "Star color_Yellowish-White"
]
input_data[4 + color_features.index(f"Star color_{star_color}")] = 1

# Mapear la categoría de la estrella a la posición correspondiente
category_features = [
    "Star category_Brown Dwarf", "Star category_Hypergiant", "Star category_Main Sequence",
    "Star category_Red Dwarf", "Star category_Supergiant", "Star category_White Dwarf"
]
input_data[16 + category_features.index(f"Star category_{star_category}")] = 1

# Botón de predicción
if st.button("Predecir Tipo de Estrella"):
    # Realizar la predicción
    prediction = model.predict([input_data])
    star_type = prediction[0]

    if star_type == 0:
        star_result= "Clase G."
        star_descrp= "El Sol, nuestra estrella, pertenece a esta clase. Aunque parecen tranquilas, su actividad magnética puede generar enormes tormentas solares que afectan a los planetas cercanos."
    elif star_type == 1:
        star_result = "Clase A."
        star_descrp= "Son las estrellas más fácilmente visibles a simple vista desde la Tierra debido a su brillo y luminosidad. Sirio, la estrella más brillante del cielo nocturno, es de tipo espectral A."
    elif star_type == 2:
        star_result = "Clase B."
        star_descrp= "Las estrellas de tipo B son responsables de ionizar las nebulosas cercanas, haciéndolas brillar intensamente. Un ejemplo famoso es Rigel, la estrella más brillante de la constelación de Orión."
    elif star_type == 3:
        star_result = "Clase F."
        star_descrp= "Estas estrellas están en un punto intermedio en cuanto a temperatura y tamaño. Son clave en estudios de evolución estelar, ya que algunas de ellas tienen planetas en su zona habitable."
    elif star_type == 4:
        star_result = "Clase O."
        star_descrp= "Son las estrellas más calientes, brillantes y masivas, pero también las menos comunes. Su vida útil es extremadamente corta en términos cósmicos, de apenas unos millones de años. Estas estrellas suelen terminar en supernovas espectaculares."
    elif star_type == 5:
        star_result = "Clase M."
        star_descrp= "Son las más comunes en el universo, representando más del 70% de las estrellas. Muchas son enanas rojas, pequeñas y longevas, con vidas que pueden durar billones de años. Próxima Centauri, la estrella más cercana a nosotros, es de este tipo."
    elif star_type == 6:
        star_result = "Clase K."
        star_descrp= "Las estrellas de tipo K suelen ser más longevas que las de tipo G, lo que las convierte en candidatas ideales para albergar sistemas planetarios donde pueda surgir vida."


    # Mostrar el resultado
    st.success(f"El modelo predice que el tipo de estrella es: **{star_result}** {star_descrp}")

    # Mostrar la imagen correspondiente
    image_path = f"img/{star_type}_star_image.jpg"  # La imagen debe estar en la carpeta 'img'
    try:
        st.image(image_path, caption=f"Imagen representativa de una estrella tipo {star_result}", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró la imagen para este tipo de estrella. Por favor, verifica que las imágenes estén en la carpeta 'img'.")
