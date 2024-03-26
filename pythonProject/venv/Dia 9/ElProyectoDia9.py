from _datetime import datetime
import os
import re
import time

def verificar_ns(texto):
    patron = r'[N][a-zA-Z]{3}-[0-9]{4}'
    busqueda = re.search(patron, texto)
    if busqueda != None:
        # print(busqueda)
        # print("Ok")
        numero_serie = busqueda.group()
        # print(numero_serie)
        return [archivo, numero_serie]
    # else:
    #     print("Incorrecto")

def listar_archivos_directorio(directorio):
    archivos = []
    for directorio_raiz, directorios, archivos_en_directorio in os.walk(directorio):
        for archivo in archivos_en_directorio:
            ruta_completa = os.path.join(directorio_raiz, archivo)
            archivos.append(ruta_completa)
    return archivos
# PC
carpeta_principal = 'C:\\Users\\joalr\\PycharmProjects\\PythonTotal\\pythonProject\\venv\\Dia 9\\ProyectoDia9\\Mi_Gran_Directorio'

# Laptop
# carpeta_principal = 'C:\\Users\\joalr\\PycharmProjects\\pythonProject\\venv\\Dia 9\\ProyectoDia9\\Mi_Gran_Directorio'
lista_archivos_serie = []
archivos_en_directorio = listar_archivos_directorio(carpeta_principal)

# Iniciando cronometro.
inicio = time.time()

# Obteniendo Fecha
fecha_busqueda = datetime.now()
fecha_formateada = fecha_busqueda.strftime('%d/%m/%y')
print('----------------------------------------------------\nFecha de busqueda:',fecha_formateada, '\n')
print('''ARCHIVO		NRO. SERIE
-------		----------
''')

# Iniciando Busqueda
for archivo in archivos_en_directorio:
    lectura = open(archivo, 'r')
    # Abriendo archivos para leer.
    texto = lectura.read()
    # Leyendo archivos.
    archivo_verificado = verificar_ns(texto)

    # Verificando si tiene el patron con el metodo verificar_ns
    if archivo_verificado != None:

        numero_serie = archivo_verificado[1]
        # Almacenando localmente los numeros de serie

        nombre_archivo = os.path.basename(archivo_verificado[0])
        # Almacenando localmente los nombres de archivos.

        lista_archivos_serie.append([nombre_archivo, numero_serie])

for na, ns in lista_archivos_serie:
    print(f'{na} - {ns} ')

# Finalizanco cronometro.
fin = time.time()
duracion = fin - inicio

print('\nNúmeros encontrados:', len(lista_archivos_serie), '\nDuracion:',duracion, '\n----------------------------------------------------')





impresion1 = '''----------------------------------------------------
Fecha de búsqueda: 

ARCHIVO		NRO. SERIE
-------		----------
{}	{}

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------'''

# print("Mis numeros son {} y {}".format(x,y))