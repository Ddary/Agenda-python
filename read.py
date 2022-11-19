import os

archivos = os.listdir("almacenamiento")

print(archivos)

for archivo in archivos:
    file = open("almacenamiento/" + archivo,  "r")

    print(file.read())
    file.close()
