import customtkinter
import tkinter

FUENTE_ESTANDAR = ("Roboto", 12)
FUENTE_PEQUENA = ("Roboto", 10)
FUENTE_GRANDE = ("Roboto", 14)

SEPARACION_DISTANCIA_X = 7
SEPARACION_DISTANCIA_Y = 26

LARGO_LINEA_ENTRADAS = 150
ALTURA_CAJA_ENTRADA = 20

SEPARACION_ENTRE_CAJAS = 70

def nuevaEntrada(master, titulo = "", distanciaX = 0, distanciaY = 0, separacionDistanciaX = SEPARACION_DISTANCIA_X, separacionDistanciaY = SEPARACION_DISTANCIA_Y, anchor = tkinter.CENTER, placeholder = ""):
    label = customtkinter.CTkLabel(
        master = master,
        text = titulo,
        text_font = FUENTE_PEQUENA,
        anchor = tkinter.W
    )
    label.place(x=distanciaX,y=distanciaY)

    posicionXCaja = distanciaX + separacionDistanciaX
    posicionYCaja = distanciaY + separacionDistanciaY

    entry = customtkinter.CTkEntry(
        master = master,
        border_width = 0,
        width = LARGO_LINEA_ENTRADAS,
        text_font = FUENTE_PEQUENA,
        fg_color = None,
        placeholder_text = placeholder
    )
    entry.place(x = posicionXCaja, y = posicionYCaja, anchor = anchor)

    line = customtkinter.CTkFrame(
        master = master,
        width = LARGO_LINEA_ENTRADAS,
        height = 2,
        corner_radius = 0
    )
    line.place(x = posicionXCaja, y = posicionYCaja + ALTURA_CAJA_ENTRADA)

    return entry