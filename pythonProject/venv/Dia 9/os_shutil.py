import os
import shutil
import send2trash

# print(os.getcwd())
# archivo = open('curso.txt', 'w')
# archivo.write('texto de prueba')
# archivo.close()
# print(os.listdir())
# Aqui vemos el archivo en la lista de archivos del directorio actual.


# shutil.move('curso.txt', 'C:\\users\\joalr\\Desktop')
# Moviendo archivo de carpeta

# os.rmdir()
# Elimina carpeta vacia.

# shutil.rmtree()
# Elimina carpeta con todo su contenido DE FORMA IRREVERSIBLE.
# PELIGROSO!!!

# send2trash.send2trash('curso.txt')
# # Elimina y manda a la papelera de reciclaje.


ruta = "C:\\Users\\joalr\\Desktop\\Carpetas\\"
print(next(os.walk(ruta)))

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print(f'Los archivo son:')
    for ar in archivo:
        # print(f'\t{ar}')
        if ar.startswith('20'):
            print(f'\t{ar}')