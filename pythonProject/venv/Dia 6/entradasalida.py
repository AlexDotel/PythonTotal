mi_archivo = open('prueba.txt')

# print(mi_archivo.read())

unalinea = mi_archivo.readline()
print(unalinea.upper)

unalinea = mi_archivo.readline()
print(unalinea)

unalinea = mi_archivo.readline()
print(unalinea)

for l in mi_archivo:
    print(l)

mi_archivo.close()

# El archivo es una coleccion de lineas, podemos iterar en el.