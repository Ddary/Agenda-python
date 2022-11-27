import os 

class Usuario:

    def __init__(self, nombreCompleto = "", username = "", mail = "", web = ""):
        self.nombreCompleto = nombreCompleto
        self.username = username
        self.mail = mail
        self.web = web


    def agregar(self):
        nombreArchivo = self.username + ".txt"
        file = open("almacenamiento/" + nombreArchivo,  "w")
        file.write(self.nombreCompleto + ", " + self.username + ", " +  self.mail + ", " + self.web)

        file.close()

    def cargarDesdeArchivo(self, rutaArchivo):
        file = open(rutaArchivo, "r")
        contenido = file.readline()
        informacion = contenido.split(", ")
        self.nombreCompleto = informacion[0]
        self.username = informacion[1]
        self.mail = informacion[2]
        self.web = informacion[3]

        file.close()

    def eliminar(self):
        nombreArchivo = self.username + ".txt"
        os.remove("almacenamiento/" + nombreArchivo)
       