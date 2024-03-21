archivo = open('Prueba.txt', 'r')
# Solo nos permite leer, es el que viene por defecto

archivo = open('Prueba.txt', 'w')
# Solo nos permite escritura, si el archivo existe es vaciado, y sino existe lo crea

archivo = open('Prueba.txt', 'a')
# Solo nos permite leer., escribe al final del archivo, mantiene el contenido original


archivo = open('Prueba.txt', 'w')
archivo.write('''Nuevo Texto 1
Segunda Linea
Tercer Linea''')
archivo.close()


archivo_dos = open('Prueba2.txt', 'w')
archivo_dos.writelines(['Lin1', 'Lin2', 'Lin3'])
# Este metodo escribe las 3 lineas juntas en el texto, pero realmenre crea una lista de 3 items.
# Es poco util, mejor hacer un for para recorrer una lista de lineas.


archivo = open('PruebaLineas.txt', 'w')
lista = ['Lin1', 'Lin2', 'Lin3']
for i in lista:
    archivo.write( i + '\n')
    print( i + '\n')
# Esta forma seria mas productiva de ejecutar para escribir lineas con saltos.


archivo = open('PruebaLineas.txt', 'a')
archivo.write('Hasta Luego.')
# Agrega una linea al final, sin formatear el archivo.
