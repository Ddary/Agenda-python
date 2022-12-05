import tkinter
import customtkinter
import interfaz
import tabla
import usuario

customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")

ventana = customtkinter.CTk()
ventana.geometry("1000x500")
ventana.title("Agenda de Usuarios")
ventana.resizable(False, False)

formulario = customtkinter.CTkFrame(master=ventana,
                               width=210,
                               height=500,
                               corner_radius=10)
formulario.place(x=0)
# formulario.pack(padx=20, pady=20)

cajaNombreCompleto = interfaz.nuevaEntrada(
    formulario,
    titulo = "Nombre Completo",
    distanciaX = 20,
    distanciaY = interfaz.SEPARACION_ENTRE_CAJAS,
    anchor = tkinter.NW
)

cajaUsername = interfaz.nuevaEntrada(
    formulario,
    titulo = "Username",
    distanciaX = 20,
    distanciaY = 2 * interfaz.SEPARACION_ENTRE_CAJAS,
    anchor = tkinter.NW
)

cajaCorreoElectronico = interfaz.nuevaEntrada(
    formulario,
    titulo = "Correo Electrónico",
    distanciaX = 20,
    distanciaY = 3 * interfaz.SEPARACION_ENTRE_CAJAS,
    anchor = tkinter.NW
)

cajaPaginaWeb = interfaz.nuevaEntrada(
    formulario,
    titulo = "Página Web",
    distanciaX = 20,
    distanciaY = 4 * interfaz.SEPARACION_ENTRE_CAJAS,
    anchor = tkinter.NW
)

botonGuardar = customtkinter.CTkButton(
    master = formulario,
    width = 80,
    height = 35,
    text = "Guardar"
)
botonGuardar.place(x = 20, y = 6 * interfaz.SEPARACION_ENTRE_CAJAS)

botonEliminar = customtkinter.CTkButton(
    master = formulario,
    width = 80,
    height = 35,
    text = "Eliminar"
)
botonEliminar.place(x = 110, y = 6 * interfaz.SEPARACION_ENTRE_CAJAS)

panelDerecho = customtkinter.CTkFrame(
    master = ventana,
    width = 789,
    height = 500,
    corner_radius = 0,
    bg_color = None,
    fg_color = None
)
panelDerecho.place(x = 211)

titulo = customtkinter.CTkLabel(
    master = panelDerecho,
    text = "Agenda de Usuarios",
    text_font = interfaz.FUENTE_GRANDE
)
titulo.place(x = 300, y = 10)

cajaBuscar = interfaz.nuevaEntrada(
    panelDerecho,
    placeholder = "Username",
    distanciaX = 319,
    distanciaY = 5.5 * interfaz.SEPARACION_ENTRE_CAJAS,
    anchor = tkinter.NW
)

botonBuscar = customtkinter.CTkButton(
    master = panelDerecho,
    width = 80,
    height = 35,
    text = "Buscar"
)
botonBuscar.place(x = 354, y = 6.4 * interfaz.SEPARACION_ENTRE_CAJAS)

textbox = customtkinter.CTkTextbox(
    master = panelDerecho,
    width = 780,
    height = 5 * interfaz.SEPARACION_ENTRE_CAJAS,
    fg_color = "gray10",
    text_font = ("Consolas", 11)
)
textbox.place(x = 5, y = 50)

tablaUsuarios = tabla.Tabla(
    textbox = textbox,
    usuarios = [
        usuario.Usuario(
            "Daniel Marcano",
            "n00best",
            "daniel@ejemplo.com",
            "daniel.com"
        ),

        usuario.Usuario(
            "Dariannys Jose Gonzalez Solis",
            "dary12345620405080",
            "dary@ejemplo.com",
            "dary.com"
        )
    ]
)

tablaUsuarios.renderizar()

ventana.mainloop()