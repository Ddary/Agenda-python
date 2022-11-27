from usuario import Usuario 
from tkinter import *
from tkinter import messagebox as mb
import os

editandoUsuario = False 

def guardar():
    global editandoUsuario
    username = cajaUsername.get()

    if username == "":
        mb.showerror("Datos inválidos", "El username es obligatorio")
        return 

    if not editandoUsuario and existe(username):
        mb.showerror("Datos inválidos", "El username " + username + " ya existe")
        return

    usuario = Usuario( cajaNombre.get(), cajaUsername.get(), cajaMail.get(), cajaWeb.get())
    usuario.agregar()
    mb.showinfo("Guardado", "El usuario fue guardado con éxito") 
    limpiar()
    editandoUsuario = False
    consultar()

def limpiar():
    cajaUsername.config(state = "normal")
    botonEliminar.config(state = "disabled")
    cajaNombre.delete(0, "end")
    cajaUsername.delete(0, "end")
    cajaMail.delete(0, "end")
    cajaWeb.delete(0, "end")

def limpiarBusqueda():
    cajaEditar.delete(0, "end")

def consultar():
    listaConsulta = Text(ventana)
    listaConsulta.insert(INSERT, "Nombre Completo\t\tUsername\t\tMail\t\tWeb\n")

    archivos = os.listdir("almacenamiento")
    for nombreArchivo in archivos:
        usuario = Usuario()
        usuario.cargarDesdeArchivo("almacenamiento/" + nombreArchivo)
        listaConsulta.insert(INSERT, usuario.nombreCompleto + "\t\t" + usuario.username + "\t\t" + usuario.mail + "\t\t" + usuario.web + "\n")
    listaConsulta.grid(row = 28, column = 1, columnspan = 4) 

def buscar():
    global editandoUsuario
    username = cajaEditar.get()
    if existe(username):
        limpiar()
        editandoUsuario = True
        usuario = Usuario()
        usuario.cargarDesdeArchivo("almacenamiento/" + username + ".txt")
        cajaNombre.insert(0, usuario.nombreCompleto)
        cajaUsername.insert(0, usuario.username)
        cajaMail.insert(0, usuario.mail)
        cajaWeb.insert(0, usuario.web)

        cajaUsername.config(state = "readonly")
        botonEliminar.config(state = "normal")

        limpiarBusqueda()
    else:
        mb.showerror("Busqueda", "El username " + username + " no fue encontrado")

def eliminar():
    global editandoUsuario
    username = cajaUsername.get()
    continuar = mb.askyesno("Eliminar Usuario", "¿Estás seguro que deseas eliminar al usuario: " + username + "?")
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

ventana = Tk()
ventana.config()

colorFondo = "#C69749"
colorLetra = "#FFF"

ventana.title("Agenda de Usuarios")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)

titulo = Label(ventana, text= "Agenda de Usuarios", bg = colorFondo, fg = colorLetra, font =("Roboto 16") )
titulo.grid(row=1, column=2, columnspan = 2)

nombreCompletoLabel = Label(ventana, text= "Nombre Completo", bg = colorFondo, fg = colorLetra, font =("Roboto 13"))
nombreCompletoLabel.grid(row = 4, column = 1)
cajaNombre = Entry(ventana)
cajaNombre.grid(row = 4, column = 2, columnspan = 2)

usernameLabel = Label(ventana, text= "Username", bg = colorFondo, fg = colorLetra, font =("Roboto 13"))
usernameLabel.grid(row = 6, column = 1)
cajaUsername = Entry(ventana)
cajaUsername.grid(row = 6, column = 2, columnspan = 2)

mailLabel = Label(ventana, text= "Mail", bg = colorFondo, fg = colorLetra, font =("Roboto 13"))
mailLabel.grid(row = 8, column = 1)
cajaMail = Entry(ventana)
cajaMail.grid(row = 8, column = 2, columnspan = 2)

webLabel = Label(ventana, text= "Página Web", bg = colorFondo, fg = colorLetra, font =("Roboto 13"))
webLabel.grid(row = 10, column = 1)
cajaWeb= Entry(ventana)
cajaWeb.grid(row = 10, column = 2, columnspan = 2)

botonGuardar = Button(ventana, text= "Guardar", bg= "#735F32", fg= "white", command= guardar)
botonGuardar.grid(row= 12, column= 2)

botonEliminar = Button(ventana, text= "Eliminar", bg= "#735F32", fg= "white", command= eliminar)
botonEliminar.grid(row= 12, column= 3)
botonEliminar.config(state = "disabled")

cajaEditar= Entry(ventana)
cajaEditar.grid(row = 4, column = 4)
botonEditar = Button(ventana, text= "Buscar", bg= "#735F32", fg= "white", command= buscar)
botonEditar.grid(row= 6, column= 4)

consultar()
ventana.mainloop()