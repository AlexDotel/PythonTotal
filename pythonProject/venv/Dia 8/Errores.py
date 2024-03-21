def sumar():
    num1 = int(input('Escribe un numero: '))
    num2 = int(input('Escribe un numero: '))

    resultado = num1 + num2
    print(resultado)
    print('Gracias por sumar'+n1)
try:
    # Intento.
    sumar()
except ValueError:
    # Como manejar errores epecificos
    print('Los tipos de datos no coindicen')
except:
    # Manejar error
    print('Algo no esta bien')
else:
    # Hiciste todo bien
    print('Hiciste todo bien')
finally:
    # Que hacer, este mal o bien.
    print('Eso fue todo')


def pedir_numero():
    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Eso no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break
    print('Gracias')

pedir_numero()