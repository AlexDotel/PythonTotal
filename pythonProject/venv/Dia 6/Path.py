from pathlib import Path

# De esta forma funciona en cualquier sistema operativo:
carpeta = Path('C:/Users/joalr/Desktop/RutillaPython')
# Incluso sin el C: habitual de Windows.
archivo = carpeta / 'otro.txt'

mi_archivo = open(archivo)
print('Primero: ', mi_archivo.read())

# Forma aun mas eficiente de trabajarlo.
archivo_dos = Path('C:/Users/joalr/Desktop/RutillaPython') / 'otro.txt'

mi_archivo_dos = open(archivo_dos)
print('Segundo: ', mi_archivo_dos.read())