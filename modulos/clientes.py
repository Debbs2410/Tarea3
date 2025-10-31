import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_info_cliente(Id_cliente):
    """
    Muestra la información del cliente en el área principal de la app.
    """
    if Id_cliente is None:
        st.info("Usuario no identificado.")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(
        "SELECT Usuario, Correo, Telefono, Edad FROM Clientes WHERE Id_cliente = %s",
        (Id_cliente,)
    )
    cliente = cursor.fetchone()
    conexion.close()

    if cliente:
        st.subheader("Información del Cliente")
        st.write(f"**Nombre:** {cliente['Usuario']}")
        st.write(f"**Correo:** {cliente['Correo']}")
        st.write(f"**Teléfono:** {cliente['Telefono']}")
        st.write(f"**Edad:** {cliente['Edad']} años")
    else:
        st.info("Cliente no encontrado.")


def agregar_cliente(usuario, contrasena, correo, telefono, edad):
    """
    Inserta un nuevo cliente en la tabla Clientes desde la app.
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
