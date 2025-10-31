# app.py
import streamlit as st
from modulos.venta import mostrar_venta  # Importamos la función mostrar_venta del módulo venta
from modulos.login import login

# Verificamos si existe la variable de sesión
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False

# Si la sesión está iniciada
if st.session_state["sesion_iniciada"]:
    # Mostrar el menú lateral
    opciones = ["Ventas", "Otra opción"]  # Agrega más opciones si las necesitas
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Mostramos el contenido según la opción elegida
    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")  # Aquí podrías agregar más secciones

# Si la sesión no está iniciada, mostrar el login
else:
    login()

