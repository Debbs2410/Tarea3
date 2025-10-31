import streamlit as st
from modulos.config.conexion import obtener_conexion

def agregar_cliente(usuario, contrasena, correo, telefono, edad):
    """
    Inserta un nuevo cliente en la tabla Clientes.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        query = """
        INSERT INTO Clientes (Usuario, Contraseña, Correo, Telefono, Edad)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (usuario, contrasena, correo, telefono, edad))
        conexion.commit()
        st.success(f"Cliente '{usuario}' agregado correctamente.")
    except Exception as e:
        st.error(f"No se pudo agregar el cliente: {e}")
    finally:
        conexion.close()
