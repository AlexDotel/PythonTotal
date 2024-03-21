# EJERCICIO 2

def deletrear(palabra):
    lista = []
    for l in palabra:
        letra = l.lower()
        if letra not in lista:
            lista.append(letra)
        else: pass
    lista.sort()
    return lista

print(deletrear(input('Escribe una palabra a deletrear y organizar alfabeticamente')))
