from random import *

# Lanza un int aleatorio
numero = randint(1,20)
print(numero)


# Lanza un float aleatorio
numero = uniform(1,5)
print(numero)

# Lanza una fraccion entre 0 y 1 de forma aleatoria
numero = random()
print(numero)

# Elegir un elemento aleatorio de una lista
colores = ['rojo','azul','blanco']
color = choice(colores)
print(color)

# Elegir un elemento aleatorio de una palabra
abc = 'abcdefghijk'
letra = choice(abc)
print(letra)

# Mezclar o desordenar una lista

numeros = list(range(5,50,5))
shuffle(numeros) #No devuelve nada, solo modifica la variable.
print(numeros)

