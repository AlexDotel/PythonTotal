from os import system
import os
from pathlib import Path, PureWindowsPath
import shutil

ruta_principal = Path(Path.home(),'Recetas')

def saludar():
    print('Hola, bienvenido al recetario.')

def mostrar_ruta():
    print(f'Las rescetas estan en: {ruta_principal}')

def contar_resetas(ruta):
    cantidadrecetas = 0
    for receta in ruta.glob('**/*.txt'):
        cantidadrecetas += 1
    mensaje = f'Este recetario consta de {cantidadrecetas} recetas'
    print (mensaje)
    return mensaje

def programa():
    seleccion = 0
    rango = range(7)
    while(seleccion not in rango or seleccion == 0):
        print(f'''¿Que quieres hacer?
    1. Leer Receta
    2. Crear Receta
    3. Crear Categoria
    4. Eliminar receta
    5. Eliminar categoria
    6. Finalizar Programa''')
        seleccion = int(input('Elige una opcion: '))
    if seleccion == 1:
        recorrer_carpetas(seleccion, ruta_principal)
    if seleccion == 2:
        recorrer_carpetas(seleccion, ruta_principal)
    if seleccion == 3:
        manejar_categorias(seleccion, ruta_principal)
    if seleccion == 4:
        print('seleccion: ',seleccion)
        recorrer_carpetas(seleccion, ruta_principal)
    if seleccion == 5:
        manejar_categorias(seleccion, ruta_principal)
    if seleccion == 6:
        print('Gracias por usar nuestro recetario, hasta pronto.')
        exit()

def manejar_categorias(seleccion, ruta_principal):

    if seleccion == 5:
        #ELIMINAMOS CATEGORIA
        eliminar_categoria(ruta_principal)

    if seleccion == 3:
        #CREAMOS CATEGORIA
        nombre_nueva_categoria = str(input('Escribe nombre de la nueva categoria: '))
        ruta_nueva_categoria = Path(ruta_principal,nombre_nueva_categoria)
        #Definimos la ruta que queremos crear, aun no la creamos.
        crear_categoria(ruta_nueva_categoria)


def eliminar_categoria(ruta):
    listaCategorias = []
    contador = 1;
    for i in ruta.glob('*'):
        # print(i)
        listaCategorias.append(i.name)
    for i in listaCategorias:
        print(f'{contador}. {i}')
        contador += 1
    categoria_seleccionada = int(input('Seleccione la categoria que desea eliminar: '))
    carpeta = listaCategorias[categoria_seleccionada - 1]
    ruta_a_eliminar = Path(ruta, carpeta)
    shutil.rmtree(ruta_a_eliminar)
    print(f'La categoria {carpeta}, se elimino correctamente.')
    fin_programa()


def crear_categoria(ruta_nueva_categoria):
    ruta_nueva_categoria.mkdir()
    #Con este comando creamos la ruta antes definida.
    print(f'La categoria, fue creada con exito.')

    fin_programa()

def recorrer_carpetas(seleccion, ruta):
    print('Recorriendo Carpetas')
    listaCategorias = []
    contador = 1;
    for i in ruta.glob('*'):
        # print(i)
        listaCategorias.append(i.name)
    for i in listaCategorias:
        print(f'{contador}. {i}')
        contador += 1
    if seleccion == 1 or seleccion == 4 : recorrer_recetas(seleccion, ruta, listaCategorias, contador)
    if seleccion == 2 : crear_receta(ruta, listaCategorias)

def crear_receta(ruta, listaCategorias):
    print('CREAR RECETAS')
    try:
        seleccion = int(input('Elige una categoria: '))
    except OSError as e:
        print(f"Error al seleccionar su categoria.")
    # print(seleccion)
    carpeta = listaCategorias[seleccion-1]
    ruta_categoria = Path(ruta, carpeta)
    # print('ruta_nueva_receta',ruta_categoria)

    nombre_receta =  str(input('Escribe el nombre de la receta: '))+'.txt'
    contenido_receta =  str(input('Escribe el contenido de la receta: '))
    ruta_nueva_receta = Path(ruta_categoria, nombre_receta)
    # print('ruta:' ,ruta_nueva_receta)

    archivo = open(ruta_nueva_receta, 'w')
    archivo.write(contenido_receta)
    archivo.close()

    archivo = open(ruta_nueva_receta)
    print(archivo.read())

    fin_programa()

def recorrer_recetas(accion, ruta, listaCategorias, contador):
    try:
        seleccion = int(input('Elige una categoria: '))
    except OSError as e:
        print(f"Error al seleccionar su categoria.")

    # print(seleccion)
    carpeta = listaCategorias[seleccion-1]
    ruta_carpeta = Path(ruta, carpeta)
    if seleccion not in range(contador):
        programa()
    else:
        escoger_recetas(accion, ruta_carpeta)

def escoger_recetas(accion, ruta_carpeta):
    # print('Carpeta:', ruta_carpeta)
    listaRecetas = []
    contador = 1;
    for i in ruta_carpeta.glob('*.txt'):
        listaRecetas.append(i.name)
    if listaRecetas != []:
        for i in listaRecetas:
            print(f'{contador}. {i}')
            contador += 1
        accion_receta(accion, listaRecetas, ruta_carpeta)
    else:
        print('No hay recetas en esta categoria')
        fin_programa()

def accion_receta(accion, listaRecetas, ruta_carpeta):
    seleccion = int(input('Elige una receta: '))
    nombre_receta = listaRecetas[seleccion-1]
    receta_seleccionada = Path(ruta_carpeta,nombre_receta)
    if accion == 1 : print(receta_seleccionada.read_text())
    if accion == 4 :
        print(receta_seleccionada)
        try:
            receta_seleccionada.unlink()
            print(f"El archivo {receta_seleccionada} ha sido eliminado correctamente.")
        except OSError as e:
            print(f"Error al eliminar el archivo {receta_seleccionada}: {e.strerror}")

    fin_programa()


def fin_programa():
    # FINALIZANDO O VOLVIENDO
    respondio = False
    while respondio == False:
        seguir = str(input('¿Desea CONTINUAR en el recetario? S/N'))
        if seguir.upper() == 'S':
            system('cls')
            respondio = True
            programa_general()
        elif seguir.upper() == 'N':
            system('cls')
            print('Hasta luego, gracias por usar nuestro recetario')
            respondio = True
            break


def programa_general():
    saludar()
    mostrar_ruta()
    contar_resetas(ruta_principal)
    programa()


programa_general()