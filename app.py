import os

CARPETA='contactos/'

def app():
    crear_directorio()


def crear_directorio():
    if not os.path.exists(CARPETA):
    #crear carpeta
        os.makedirs(CARPETA)


app()