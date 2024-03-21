def funcion():
    return 4
# Devuelve el 4 y lo almacena en memoria.

def generador():
    yield 4
# Genera el 4 solo cuando sea necesario.

print(funcion())
print(generador())
print('')
print(next(generador()))

def listando():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def generando():
    for x in range(1,5):
        yield x * 10

gg = generando()

print(' --- LISTAS EJEMPLOS --- ')
print(listando())
print(generando())
print(next(gg))
print(next(gg))
print(next(gg))
print(next(gg))
# print(next(gg)) #Aqui ya no tiene mas que generar.


def funcion_generadora():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

generadora = funcion_generadora()

print(next(generadora)) # Imprimer solo el primer yield donde x = 1
print(next(generadora)) # Recuerda donde se quedo, asi que imprimer el siguiente yield (2)
print(next(generadora)) # Lo mismo, imprime el ultimo y 3er yield.
