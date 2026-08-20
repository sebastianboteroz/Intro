import streamlit as st
from PIL import Image

st.title("La primera app de Sebastián en Streamlit")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open("piedras.jpg")
st.image(image, caption="Interfaces Multimodales")


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2= st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experienica de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp: 
  st.write('Correcto!')

with col2: 
  st.subheader("Esta es la segunda columna")
  modo = st.radio

