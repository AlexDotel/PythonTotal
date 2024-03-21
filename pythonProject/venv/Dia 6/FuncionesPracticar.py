import os
from pathlib import Path

def abrir_leer(archivo):
    archivo = open(archivo)
    lectura = archivo.read()
    return lectura


def sobrescribir(archivo):
    archivo = open(archivo, 'w')
    archivo.write("contenido eliminado")

def registro_error(archivo):
    archivo = open(archivo, 'a')
    archivo.write( "se ha registrado un error de ejecución")
    archivo.close()

def mparents():
    ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
    carpeta = ruta.parents[3]
    # Al parecere esta funcion nos devuelve de origen hacia adentro.
    print(carpeta)

mparents()