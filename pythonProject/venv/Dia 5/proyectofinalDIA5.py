from random import *


# JUEGO DEL AHORCADO

lista_palabras = ['manzana', 'mango', 'banana', 'uva', 'mandarina', 'pera', 'melocoton', 'melon']
palabra = choice(lista_palabras)

intentos = len(palabra)
pista = list('_' * len(palabra))
confirmacion = ''.join(pista)
print(confirmacion)

letras_correctas = []
letras_incorrectas = []

def validarLetra():
    # print('Ejecucion validar letra')


    validez = False
    while validez == False:

        entrada = input('Escribe una letra: ')

        if entrada.isalpha() and len(entrada) == 1:
            validez = True
            # print(f'Haz introducido un caracter valido.')
            return entrada
        else:
            print('Caracter incorrecto, debe ser una unica letra.')

def letra_en_palabra(letra):
    global intentos
    global pista

    # print('Ejecucion letra en palabra')

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                pista[i] = letra
        confirmacion = ''.join(pista)
        print(confirmacion)


        if letra not in letras_correctas:
            letras_correctas.append(letra)
            print(f'La letra {letra}, es valida.')
            print(f'Te quedan {intentos} intentos')
        else:
            print('Ya has acertado esta letra, intentalo con otra.')
            print(f'Te quedan {intentos} intentos')
    else:
        # print(pista)
        if letra not in letras_incorrectas:
            letras_incorrectas.append(letra)
            print(f'La letra {letra}, es invalida.')
            print(f'Veces que te has equivocado: {len(letras_incorrectas)}')
            print(f'Estas son las letras con las que te has equivocado: {letras_incorrectas}')
            intentos -= 1
            print(f'Te quedan {intentos} intentos')
        else:
            print('Ya es fallado con esta letra, intentalo de nuevo.')
            print(f'Te quedan {intentos} intentos')

while intentos > 0:
    letra = validarLetra()
    letra_en_palabra(letra)
    confirmacion = ''.join(pista)
    print(confirmacion)
    if confirmacion == palabra:
        print('Ganaste!')
        break

if intentos == 0: print('Se termino el juego, has perdido')
