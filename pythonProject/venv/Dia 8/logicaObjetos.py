"""
Entendiendo la logica de los objetos.
"""

def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mi_funcion = mayuscula
#Se puede asignar una funcion a una variable.

def una_funcion(funcionx):
    return funcionx
# Podemos pedir como parametro de una funcion, a otra.

def cambiar_letra(tipo):
# Aqui creamos varias funciondes dentro de una funcion
# Con el fin de devolver la funcion que el usuario pida
# A la variable que se le asigne... En este ejemplo, may
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if(tipo == 'may'):
        return mayuscula
    elif (tipo == 'min'):
        return minuscula

operacion = cambiar_letra('may')

operacion('palabra')

#
# una_funcion(mayuscula('Hola'))
# mayuscula('Hola')
# minuscula('Hola')