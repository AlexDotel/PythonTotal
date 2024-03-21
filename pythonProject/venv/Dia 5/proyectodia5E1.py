# EJEICICIO NUMERO 01

def devolver_distintos(num1, num2, num3):

    # Con tupla

    tupla = (num1,num2,num3)
    total = num1+num2+num3

    menor = min(tupla)
    mayor = max(tupla)
    # medio = (num1,num2,num3) - menor - mayor

    if      total > 15: return mayor
    elif    total < 10: return menor
    else:
        if      num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3: return num1
        elif    num2 > num1 and num2 < num3 or num2 < num1 and num2 > num3: return num2
        elif    num3 > num1 and num3 < num2 or num2 < num3 and num3 > num2: return num3

print(devolver_distintos(2,4,2))


def devolver_distintos(num1, num2, num3):
    # Con lista

    lista = [num1, num2, num3]
    lista.sort()
    total = num1 + num2 + num3

    menor = lista[0]
    mayor = lista[2]
    medio = lista[1]

    if total > 15:
        return mayor
    elif total < 10:
        return menor
    else:
        return medio


print(devolver_distintos(20, 4, 2))


