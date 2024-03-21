# EJERCICIO 3

def repeticion(*args):
    previo = None
    for n in args:
        # print('numero actual',n)
        # print('numero previo',previo)
        if n == 0:
            if previo == n:
                return True
            if n != previo:
                previo = n
        else: previo = n
    return False

print(repeticion(5,6,1,0,0,9,3,5))
print(repeticion(6,0,5,1,0,3,0,1))