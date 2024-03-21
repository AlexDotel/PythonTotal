# EJERCICIO 4

def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0

    while (iteracion < numero):

        for n in range (3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(50))
print(contar_primos(100))



    # for i in range(2, numero):
    #     if numero % i == 0:
    #         print(i, 'No es primo')
    #     else:
    #         print(i,'Es primo')
    #         primos.append(i)
    # print(primos)
    # return len(primos)



