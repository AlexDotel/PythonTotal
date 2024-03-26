import os

carpeta_principal = 'C:\\Users\\joalr\\PycharmProjects\\pythonProject\\venv\\Dia 9\\ProyectoDia9\\Mi_Gran_Directorio'
print(next(os.walk(carpeta_principal)))

def listar_archivos_directorio(directorio):
    archivos = []
    for directorio_raiz, directorios, archivos_en_directorio in os.walk(directorio):
        for archivo in archivos_en_directorio:
            ruta_completa = os.path.join(directorio_raiz, archivo)
            archivos.append(ruta_completa)
    return archivos

directorio_principal = '/ruta/de/tu/directorio/principal'
archivos_en_directorio = listar_archivos_directorio(carpeta_principal)

for archivo in archivos_en_directorio:
    print(archivo)
    lectura = open(archivo, 'r')
    print(lectura.read())
