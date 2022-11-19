import os

nombreCompleto = input("Igrese nombre completo: ")
username = input("Igrese userename: ")
email = input("Igrese email: ")
paginaWeb = input("Igrese página web: ")

nombreArchivo = username + ".txt"

file = open("almacenamiento/" + nombreArchivo,  "w")
file.write(nombreCompleto + ", " + username + ", " +  email + ", " + paginaWeb)

file.close

