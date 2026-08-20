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
  modo = st.radio("Que modalidad es la principal en tu interfaz", ('visual', 'auditivo', 'táctil'))
  if modo == 'visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditivo':
    st.write('La audicion es fundamental para tu interfaz')
  if modo == 'táctil':
    st.write('El tacto es fundamental para tu interfaz')

st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')
  

