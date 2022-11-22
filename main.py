from usuario import Usuario 
from tkinter import *


def guardar():
    usuario = Usuario( cajaNombre.get(), cajaUsername.get(), cajaMail.get(), cajaWeb.get())
    usuario.agregar()
    limpiar()

def limpiar():
    cajaNombre.delete(0, "end")
    cajaUsername.delete(0, "end")
    cajaMail.delete(0, "end")
    cajaWeb.delete(0, "end")


ventana = Tk()


colorFondo = "#C69749"
colorLetra = "#FFF"

ventana.title("Agenda de Usuarios")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)

titulo = Label(ventana, text= "Agenda de Usuarios", bg = colorFondo, fg = colorLetra, font =("Roboto 16") )
titulo.grid(row=1, column=3)

nombreCompletoLabel = Label(ventana, text= "Nombre Completo", bg = colorFondo, fg = colorLetra, font =("Roboto 13"))
nombreCompletoLabel.grid(row = 4, column = 1)
cajaNombre = Entry(ventana)
cajaNombre.grid(row = 4, column = 2)

usernameLabel = Label(ventana, text= "Username", bg = colorFondo, fg = colorLetra, font =("Roboto 13"))
usernameLabel.grid(row = 6, column = 1)
cajaUsername = Entry(ventana)
cajaUsername.grid(row = 6, column = 2)

mailLabel = Label(ventana, text= "Mail", bg = colorFondo, fg = colorLetra, font =("Roboto 13"))
mailLabel.grid(row = 8, column = 1)
cajaMail = Entry(ventana)
cajaMail.grid(row = 8, column = 2)

webLabel = Label(ventana, text= "Página Web", bg = colorFondo, fg = colorLetra, font =("Roboto 13"))
webLabel.grid(row = 10, column = 1)
cajaWeb= Entry(ventana)
cajaWeb.grid(row = 10, column = 2)

botonGuardar = Button(ventana, text= "Guardar", bg= "#735F32", fg= "white", command= guardar)
botonGuardar.grid(row= 12, column= 2)


ventana.mainloop()