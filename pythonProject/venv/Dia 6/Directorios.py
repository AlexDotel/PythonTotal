import os

ruta = os.getcwd()
#Obtener directorio de trabajo actual

# ruta = os.chdir('C:\\Users\\joalr\\Desktop\\RutillaPython')
#Cambiar de directorio

# ruta = os.makedirs('C:\\Users\\joalr\\Desktop\\RutillaPython\\NuevaDesdePython')
# Crear directorio

# archivo = open('otro.txt')

print('Mi ruta: ',ruta)
# print(archivo.read())



# La ruta se divide siempre en 2 , la ruta de la carpeta y el archivo.
# Se puede obtener uno o el otro, o los dos divididos en una tupla.

ruta = 'C:\\Users\\joalr\\Desktop\\RutillaPython\\NuevaDesdePython'

# elemento = os.path.basename(ruta)

print('Nombre Archivo:',os.path.basename(ruta))
# Nombre del archivo
print('Nombre Carpeta:',os.path.dirname(ruta))
# Directorio del archivo (Carpeta)
print('Tupla del archivo y la carpeta:',os.path.split(ruta))
#Tupla del archivo y la carpeta
print(ruta)
#Ruta Original

os.rmdir(ruta)
# Elimina la carpeta indicada

