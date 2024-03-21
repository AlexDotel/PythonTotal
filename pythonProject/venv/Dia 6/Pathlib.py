from pathlib import Path, PureWindowsPath

archivo = Path('C:/Users/joalr/Desktop/RutillaPython') / 'otro.txt'
print(archivo.read_text())
# Usando pathlib no hace falta abrir el archivo para leerlo

print(archivo.name)
# Devuelve el nombre del archivo

print(archivo.suffix)
# Devuelve la extension del archivo

print(archivo.stem)
# Devuelve el nombre del archivo sin la extension

if archivo.exists():
    print('Existe')
else:
    print('No existe')
# Devuelve true si el archivo existe, y viceversa

ruta = PureWindowsPath("C:/Users/Usuario/Desktop")
#Convierte la ruta al formato de Windows nativo

print(ruta)