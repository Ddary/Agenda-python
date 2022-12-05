import customtkinter
import tkinter
import math

ANCHO_CARACTERES_TABLA=94

ANCHO_COLUMNA_NOMBRE=25
ANCHO_COLUMNA_USERNAME=22
ANCHO_COLUMNA_EMAIL=29
ANCHO_COLUMNA_WEB=18

class Tabla:
    usuarios = []
    textbox = None

    def __init__(self, textbox, usuarios = []):
        self.textbox = textbox
        self.usuarios = usuarios 

    def agregarUsuario(self, usuario):
        self.usuarios.append(usuario)
        self.renderizar()

    def agregarLinea(self, linea):
        self.textbox.insert(tkinter.INSERT, linea + "\n")

    def centrarLinea(self, linea):
        caracteresTotales = len(linea)
        espaciosEnBlanco = ANCHO_CARACTERES_TABLA - caracteresTotales

        if espaciosEnBlanco <= 0:
            return linea

        espaciosEnBlanco = math.floor(espaciosEnBlanco / 2)
        linea = " " * espaciosEnBlanco + linea

        return linea

    def formatearColumna(self, texto, tamanoColumna):
        tamanoTexto = len(texto)

        if tamanoTexto >= tamanoColumna:
            columna = texto[:tamanoColumna-5] + "." * 3 + "  "
            return columna

        espaciosEnBlanco = tamanoColumna - tamanoTexto
        columna = texto + " " * espaciosEnBlanco
        return columna

    def renderizar(self):
        self.textbox.configure(state = "normal")
        if len(self.usuarios) == 0:
            self.agregarLinea(self.centrarLinea("No hay usuarios agregados."))
            self.agregarLinea(self.centrarLinea("Intente agregando un usuario en el formulario izquierdo."))
            self.textbox.configure(state = "disabled")
            return

        self.agregarLinea(
            self.formatearColumna("Nombre Completo", ANCHO_COLUMNA_NOMBRE) +
            self.formatearColumna("Username", ANCHO_COLUMNA_USERNAME) +
            self.formatearColumna("Correo Electrónico", ANCHO_COLUMNA_EMAIL) +
            self.formatearColumna("Página Web", ANCHO_COLUMNA_WEB)
        )

        for usuario in self.usuarios:
            self.agregarLinea(
                self.formatearColumna(usuario.nombreCompleto, ANCHO_COLUMNA_NOMBRE) +
                self.formatearColumna(usuario.username, ANCHO_COLUMNA_USERNAME) +
                self.formatearColumna(usuario.mail, ANCHO_COLUMNA_EMAIL) +
                self.formatearColumna(usuario.web, ANCHO_COLUMNA_WEB)
            )

        self.textbox.configure(state = "disabled")