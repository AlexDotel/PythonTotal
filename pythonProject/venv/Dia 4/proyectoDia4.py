from random import *

minimo = 1
maximo = 10
numero = randint(minimo,maximo)
nombre = input('Escribe tu nombre: ')
if nombre == '' : nombre = 'usuario'
intentos = 4
intentosbu = 4

print(F'Hola {nombre}, piensa un numero entre el 1 y el 10, tienes {intentos} intentos para adivinarlo. ')

while intentos >= 1:
    intento = int(input('Escribe un numero: '))
    if intento > maximo or intento < minimo:
        print('El numero debe estar entre 1 y 10')
        print(f'Te quedan {intentos} intentos {nombre}')
    elif intento < numero:
        print('El numero introducido es muy pequeño')
        intentos -= 1
        print(f'Te quedan {intentos} intentos {nombre}')
    elif intento > numero:
        print('El numero introducido es muy grande')
        intentos -= 1
        print(f'Te quedan {intentos} intentos {nombre}')
    elif intento == numero:
        print(f'Has ganado {nombre}! eres un crack, solo te ha tomado {intentosbu-intentos+1} intentos')
        break
else:
    print(f'Lo siento {nombre}, no te quedan mas intentos')