import streamlit as st
from modulos.venta import mostrar_venta
from modulos.login import login
from modulos.productos import mostrar_productos
from modulos.clientes import mostrar_info_cliente  # <-- CORREGIDO

# Inicializar variables de sesión
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False
if "Id_cliente" not in st.session_state:
    st.session_state["Id_cliente"] = None

# Si la sesión está iniciada
if st.session_state["sesion_iniciada"]:
    # Mostrar info del cliente usando Id_cliente
    mostrar_info_cliente(st.session_state["Id_cliente"])

    # Menú lateral
    opciones = ["Ventas", "Productos", "Otra opción"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Mostrar contenido según la opción
    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Productos":
        mostrar_productos()
    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")

# Si no hay sesión iniciada
else:
    login()
