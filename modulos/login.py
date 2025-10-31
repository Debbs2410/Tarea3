import streamlit as st
from modulos.config.conexion import obtener_conexion
from modulos.clientes import agregar_cliente  # import para registrar clientes

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
        result = cursor.fetchone()
        return result if result else None
    finally:
        con.close()


def login():
    st.title("Inicio de sesión / Registro")

    # Selección entre login y registro
    modo = st.radio("Selecciona una opción:", ["Iniciar sesión", "Registrarse"])

    if modo == "Iniciar sesión":
        Usuario = st.text_input("Usuario", key="Usuario_login")
        Contraseña = st.text_input("Contraseña", type="password", key="Contrasena_login")
        if st.button("Iniciar sesión"):
            resultado = verificar_usuario(Usuario, Contraseña)
            if resultado:
                Id_cliente, usuario_nombre = resultado
                st.session_state["sesion_iniciada"] = True
                st.session_state["Id_cliente"] = Id_cliente
                st.session_state["usuario"] = usuario_nombre
                st.success(f"Bienvenido ({usuario_nombre}) 👋")
                st.rerun()
            else:
                st.error("❌ Credenciales incorrectas.")

    elif modo == "Registrarse":
        st.subheader("Registrar nuevo cliente")
        with st.form("form_registro", clear_on_submit=True):
            usuario = st.text_input("Usuario")
            contrasena = st.text_input("Contraseña", type="password")
            correo = st.text_input("Correo")
            telefono = st.text_input("Teléfono")
            edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
            submit = st.form_submit_button("Registrar")

            if submit:
                if usuario and contrasena and correo and telefono:
                    agregar_cliente(usuario, contrasena, correo, telefono, edad)
                    st.success("Cliente registrado correctamente. Ahora inicia sesión.")
                else:
                    st.error("Todos los campos son obligatorios.")
