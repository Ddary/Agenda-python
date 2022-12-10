import tkinter
import customtkinter
import interfaz
import tabla
import os
from usuario import Usuario
from tkinter import messagebox 

editandoUsuario = False 

def guardar():
    global editandoUsuario
    username = cajaUsername.get().strip().lower()

    if username == "":
        messagebox.showerror("Datos inválidos", "El username es obligatorio")
        return 

    if not editandoUsuario and existe(username):
        messagebox.showerror("Datos inválidos", "El username " + username + " ya existe")
        return

    usuario = Usuario(
        cajaNombreCompleto.get().strip(),
        username,
        cajaCorreoElectronico.get().strip(),
        cajaPaginaWeb.get().strip()
    )
    usuario.agregar()
    messagebox.showinfo("Guardado", "El usuario fue guardado con éxito") 
    limpiar()
    editandoUsuario = False
    consultar()

def limpiar():
    cajaUsername.configure(state = "normal")
    botonEliminar.configure(state = "disabled")
    cajaNombreCompleto.delete(0, "end")
    cajaUsername.delete(0, "end")
    cajaCorreoElectronico.delete(0, "end")
    cajaPaginaWeb.delete(0, "end")

def limpiarBusqueda():
    cajaBuscar.delete(0, "end")

def consultar():
    usuarios = []

    archivos = os.listdir("almacenamiento")
    for nombreArchivo in archivos:
        usuario = Usuario()
        usuario.cargarDesdeArchivo("almacenamiento/" + nombreArchivo)
        usuarios.append(usuario) 

    tablaUsuarios.usuarios = usuarios
    tablaUsuarios.renderizar()

def buscar():
    global editandoUsuario
    username = cajaBuscar.get().strip().lower()
    if existe(username):
        limpiar()
        editandoUsuario = True
        usuario = Usuario()
        usuario.cargarDesdeArchivo("almacenamiento/" + username + ".txt")
        cajaNombreCompleto.insert(0, usuario.nombreCompleto)
        cajaUsername.insert(0, usuario.username)
        cajaCorreoElectronico.insert(0, usuario.mail)
        cajaPaginaWeb.insert(0, usuario.web)

        cajaUsername.configure(state = "readonly")
        botonEliminar.configure(state = "normal")

        limpiarBusqueda()
    else:
        messagebox.showerror("Busqueda", "El username " + username + " no fue encontrado")

def eliminar():
    global editandoUsuario
    username = cajaUsername.get().strip().lower()
    continuar = messagebox.askyesno("Eliminar Usuario", "¿Estás seguro que deseas eliminar al usuario: " + username + "?")
    if continuar:
        usuario = Usuario()
        usuario.cargarDesdeArchivo("almacenamiento/" + username + ".txt")
        usuario.eliminar()
        limpiar()
        editandoUsuario = False
        consultar()

def existe(username):
    encontrado = False
    archivos = os.listdir("almacenamiento")
    for nombreArchivo in archivos:
        if username + ".txt" == nombreArchivo:
            encontrado = True
    return encontrado

# verificar si almecenamiento existe o crearlo si no
if not os.path.isdir("almacenamiento"):
    os.mkdir("almacenamiento")

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
    text = "Guardar",
    command = guardar
)
botonGuardar.place(x = 20, y = 6 * interfaz.SEPARACION_ENTRE_CAJAS)

botonEliminar = customtkinter.CTkButton(
    master = formulario,
    width = 80,
    height = 35,
    text = "Eliminar",
    command = eliminar
)
botonEliminar.place(x = 110, y = 6 * interfaz.SEPARACION_ENTRE_CAJAS)
botonEliminar.configure(state = "disabled")

panelDerecho = customtkinter.CTkFrame(
    master = ventana,
    width = 789,
    height = 500,
    corner_radius = 0,
    bg_color = "transparent",
    fg_color = "transparent"
)
panelDerecho.place(x = 211)

titulo = customtkinter.CTkLabel(
    master = panelDerecho,
    text = "Agenda de Usuarios",
    font = interfaz.FUENTE_GRANDE
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
    text = "Buscar",
    command = buscar
)
botonBuscar.place(x = 354, y = 6.4 * interfaz.SEPARACION_ENTRE_CAJAS)

textbox = customtkinter.CTkTextbox(
    master = panelDerecho,
    width = 780,
    height = 5 * interfaz.SEPARACION_ENTRE_CAJAS,
    fg_color = "gray10",
    font = interfaz.FUENTE_MONOESPACIO
)
textbox.place(x = 15, y = 50)

tablaUsuarios = tabla.Tabla(
    textbox = textbox,
    usuarios = []
)

consultar()

ventana.mainloop()