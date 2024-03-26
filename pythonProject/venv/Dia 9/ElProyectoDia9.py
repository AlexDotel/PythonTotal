import shutil

ruta = ('C:\\Users\\joalr\\PycharmProjects\\pythonProject\\venv\\Dia 9\\Proyecto+Dia+9.zip')
nombre_archivo = 'Proyecto+Dia+9.zip'
shutil.unpack_archive(nombre_archivo, 'ProyectoDia9', 'zip')