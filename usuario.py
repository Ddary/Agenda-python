import os 

class Usuario:

    def __init__(self, nombreCompleto, username, mail, web):
        self.nombreCompleto = nombreCompleto
        self.username = username
        self.mail = mail
        self.web = web


    def agregar(self):
        nombreArchivo = self.username + ".txt"
        file = open("almacenamiento/" + nombreArchivo,  "w")
        file.write(self.nombreCompleto + ", " + self.username + ", " +  self.mail + ", " + self.web)

        file.close()