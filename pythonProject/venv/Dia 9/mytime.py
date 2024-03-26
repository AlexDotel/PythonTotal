# # import time
import timeit


def p_for (numero):
    lista = []
    for n in range (1,numero+1):
        lista.append(n)
    # print(lista)
    return lista


def p_wile (numero):
    lista = []
    c = 0
    while c < numero:
        c += 1
        lista.append(c)
    # print(lista)
    return lista
#
#
# inicio = time.time()
# p_for(100000)
# fin = time.time()
# print(fin - inicio)
#
# inicio = time.time()
# p_wile(100000)
# fin = time.time()
# print(fin - inicio)


mi_setup = '''
def p_for (numero):
    lista = []
    for n in range (1,numero+1):
        lista.append(n)
    return lista
'''

declaracion = '''
p_for(10)
'''

duracion = timeit.timeit(declaracion, mi_setup , number= 100000)
print(duracion)

mi_setup2 = '''
def p_while (numero):
    lista = []
    c = 0
    while c < numero:
        c += 1
        lista.append(c)
    # print(lista)
    return lista
'''


declaracion2 = '''
p_while(10)
'''

duracion = timeit.timeit(declaracion2, mi_setup2 , number= 100000)
print(duracion)