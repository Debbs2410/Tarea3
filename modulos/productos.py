import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_productos():
    """Muestra todos los productos de la base de datos"""
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Productos")  # Nota la P mayúscula
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        st.subheader("Lista de productos disponibles")
        for producto in productos:
            # Usamos la columna 'Nombre' y 'Disponible'
            st.write(f"{producto['Nombre']} - Disponibles: {producto['Disponible']}")
    else:
        st.info("No hay productos disponibles.")
