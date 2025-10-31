from modulos.clientes import mostrar_info_cliente, agregar_cliente

# Menú lateral
opciones = ["Ventas", "Productos", "Cliente", "Agregar Cliente", "Otra opción"]
seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

# Mostrar contenido según la opción
if seleccion == "Ventas":
    mostrar_venta()
elif seleccion == "Productos":
    mostrar_productos()
elif seleccion == "Cliente":
    mostrar_info_cliente(st.session_state["Id_cliente"])
elif seleccion == "Agregar Cliente":
    st.subheader("Agregar un nuevo cliente")

    with st.form("form_agregar_cliente", clear_on_submit=True):
        usuario = st.text_input("Usuario")
        contrasena = st.text_input("Contraseña", type="password")
        correo = st.text_input("Correo")
        telefono = st.text_input("Teléfono")
        edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
        submit = st.form_submit_button("Agregar Cliente")

        if submit:
            if usuario and contrasena and correo and telefono:
                agregar_cliente(usuario, contrasena, correo, telefono, edad)
            else:
                st.error("Todos los campos son obligatorios.")
elif seleccion == "Otra opción":
    st.write("Has seleccionado otra opción.")
