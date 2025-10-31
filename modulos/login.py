import streamlit as st
from modulos.config.conexion import obtener_conexion
from modulos.venta import mostrar_venta

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
        result = cursor.fetchone()  # result será algo como (Id_cliente, Usuario)
        return result if result else None
    finally:
        con.close()


def login():
    st.title("Inicio de sesión")

    # 🟢 Mensaje si ya hubo conexión exitosa
    if st.session_state.get("conexion_exitosa"):
        st.success("✅ Sesión iniciada correctamente.")

    Usuario = st.text_input("Usuario", key="Usuario_input")
    Contraseña = st.text_input("Contraseña", type="password", key="Contraseña_input")

    if st.button("Iniciar sesión"):
        resultado = verificar_usuario(Usuario, Contraseña)
        if resultado:
            cliente_id, usuario_nombre = resultado  # Extraemos Id_cliente y Usuario
            st.session_state["usuario"] = usuario_nombre
            st

