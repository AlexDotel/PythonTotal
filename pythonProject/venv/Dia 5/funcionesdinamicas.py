

def check (lista):

    listacifra = []

    for numero in lista:
       if numero in range(100,1000):
           listacifra.append(numero)
       else:
           pass
    return listacifra

resultado = check([1212,122,2321,555])
print(resultado)


def todos_positivos(listanumeros):
    listabool = []
    for n in listanumeros:
        if n >= 0:
            listabool.append(True)
        else:
            listabool.append(False)

    if listabool.__contains__(False):
        return False
    else:
        return True

lista_numeros = [1, 3, -1, 2]

print(todos_positivos(lista_numeros))






lista_numeros = [1,2,400,4,-2,3,3421]

def suma_menores(lista):
    result = 0
    for n in lista:
        if n in range(1,1001):
            result += n
        else:
            pass
    return result

print(suma_menores(lista_numeros))



lista_numeros = [1,2,3,4,5,6,7,8,9]
def cantidad_pares (lista_numeros):
    listapares = []
    for n in lista_numeros:
        if n % 2 == 0:
            listapares.append(n)
    return len(listapares)


print(cantidad_pares(lista_numeros))



