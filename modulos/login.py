import streamlit as st
from modulos.config.conexion import obtener_conexion
from modulos.venta import mostrar_venta

def verificar_usuario(Usuario, Contraseña):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se puede iniciar sesión en estos momentos.")
        return None
    else:
        # ✅ Guardar en el estado que la conexión fue exitosa
        st.session_state["conexion_exitosa"] = True

    try:
        cursor = con.cursor()
        query = "SELECT Usuario, Contraseña FROM Clientes WHERE Usuario = %s AND Contraseña = %s"
        cursor.execute(query, (Usuario, Contraseña))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        con.close()


def login():
    st.title("Inicio de sesión")

    # 🟢 Mostrar mensaje persistente si ya hubo conexión exitosa
    if st.session_state.get("conexion_exitosa"):
        st.success("✅ Sesión iniciada correctamente.")

    Usuario = st.text_input("Usuario", key="Usuario_input")
    Contraseña = st.text_input("Contraseña", type="password", key="Contraseña_input")

    if st.button("Iniciar sesión"):
        tipo = verificar_usuario(Usuario, Contraseña)
        if tipo:
            st.session_state["usuario"] = Usuario
            st.success(f"Bienvenido ({Usuario}) 👋")
            st.session_state["sesion_iniciada"] = True
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")
