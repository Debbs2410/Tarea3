import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_info_cliente(usuario_id):
    """
    Muestra la información del cliente en el menú lateral usando Id_cliente.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT Usuario, Correo, Telefono, Edad 
        FROM Clientes 
        WHERE Id_cliente = %s
    """, (usuario_id,))
    cliente = cursor.fetchone()
    conexion.close()

    if cliente:
        st.sidebar.subheader("Información del Cliente")
        st.sidebar.write(f"Nombre: {cliente['Usuario']}")
        st.sidebar.write(f"Correo: {cliente['Correo']}")
        st.sidebar.write(f"Teléfono: {cliente['Telefono']}")
        st.sidebar.write(f"Edad: {cliente['Edad']} años")
    else:
        st.sidebar.info("Cliente no encontrado.")
