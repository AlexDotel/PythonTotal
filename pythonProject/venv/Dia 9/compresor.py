import shutil
import zipfile

#   ==============  COMPRESION CON ZIPFILE  ==============
# mi_zip = zipfile.ZipFile('archivoAcomprimido.zip', 'w')

# mi_zip.write('mitextoa.txt')
# mi_zip.write('mitextob.txt')

# mi_zip.close()

# ==============  DESCOMPRESION CON ZIPFILE  ==============
# zip_abierto = zipfile.ZipFile('archivoAcomprimido.zip', 'r')
# zip_abierto.extractall()

# ==============  COMPRESION CON SHUTIL  ==============
# ruta_origen = "C:\\Users\\joalr\\Desktop\\Carpetas"
# archivo_destino = 'Todo_Comprimido'
# shutil.make_archive(archivo_destino, 'zip', ruta_origen)
# # Creandolo con Shutil, se creo en la misma ruta de este script.

# ==============  COMPRESION CON SHUTIL  ==============
# shutil.unpack_archive('Todo_Comprimido.zip', 'Extracion Terminada', 'zip')