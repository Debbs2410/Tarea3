import streamlit as st
from modulos.config.conexion import obtener_conexion

def verificar_usuario(Usuario, Contraseña):
    """
    Verifica que el usuario y contraseña existan en la base de datos.
    Devuelve una tupla (Id_cliente, Usuario) si es correcto, o None si no.
    """
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se puede iniciar sesión en estos momentos.")
        return None

    try:
        cursor = con.cursor()
        query = "SELECT Id_cliente, Usuario FROM Clientes WHERE Usuario = %s AND Contraseña = %s"
        cursor.execute(query, (Usuario, Contraseña))
        result = cursor.fetchone()  # devuelve (Id_cliente, Usuario)
        return result if result else None
    finally:
        con.close()


def login():
    st.title("Inicio de sesión")

    Usuario = st.text_input("Usuario", key="Usuario_input")
    Contraseña = st.text_input("Contraseña", type="password", key="Contraseña_input")

    if st.button("Iniciar sesión"):
        resultado = verificar_usuario(Usuario, Contraseña)
        if resultado:
            Id_cliente, usuario_nombre = resultado
            st.session_state["sesion_iniciada"] = True
            st.session_state["Id_cliente"] = Id_cliente  # guardamos Id_cliente
            st.session_state["usuario"] = usuario_nombre
            st.success(f"Bienvenido ({usuario_nombre}) 👋")
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")
