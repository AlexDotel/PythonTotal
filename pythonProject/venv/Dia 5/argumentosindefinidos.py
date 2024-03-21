# *args
# *kwargs

# Aqui solo podemos sumar dos argumentos.
def suma(a,b):
    return a+b

print (suma(2,34))


# Podemos agregar argumentos, indefinidos
def sumaconargs(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print (sumaconargs(2,23,223 ))


# Podrian bien ser cualquier otra palabra en vez de args
def sumaconargs(*numeros):
    total = 0
    for arg in numeros:
        total += arg
    return total

print (sumaconargs(2,23,223 ))




def suma_cuadrados (*numeros):
    numerototal = 0
    for n in numeros:
        numerototal += n**2
    return numerototal

print(suma_cuadrados(1,2,3))




def suma_absolutos(*args):
    total = 0
    for argumento in args:
        total += abs(argumento)
    return total
print(suma_absolutos(1,2,3,-2,-1,-2))






def numeros_persona (nombre,*numeros):
    suma_numeros = 0
    for n in numeros:
        suma_numeros += n
    return f'{nombre}, la suma de tus números es {suma_numeros}'

print(numeros_persona('Josue',2,2,2,1,1,1))
