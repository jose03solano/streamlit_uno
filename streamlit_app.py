import streamlit as st

st.title("🎈 Soy Bien")
st.write(
    "Estadísticas de una salud laboral estable, y buena [clickvital](https://clickvital.com.co/)."
)


cantidad = st.slider('Selecciona la cantidad')

st.write(f'La cantidad seleccionada es {cantidad}')

for i in range(cantidad):
    st.button(f'{i}')

