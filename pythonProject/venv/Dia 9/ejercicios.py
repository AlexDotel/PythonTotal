import re

def verificar_email(email):

    patron1 = re.search('.@.', email)
    patron2 = re.search(r'\Wcom|.com.+$', email )

    if patron1 != None and patron2 != None:
    # if patron1 != None:
        print('Ok')
    else:
        print('La dirección de email es incorrecta')

verificar_email('hola@gmail.com.br')


def verificar_saludo(frase):

    patron1 = re.search('Hola', frase)

    if patron1 != None and patron1.start() == 0:
        print("Ok")
    else:
        print("No has saludado")

verificar_saludo('Hola Adios,  como estas?')



def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    busqueda = re.search(patron, cp)
    if busqueda != None:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp('2ewsa')


