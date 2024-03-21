def turnos_perfumeria():
    for i in range(1,1000):
        yield f'P-{i}'

def turnos_farmacia():
    for i in range(1,1000):
        yield f'F-{i}'

def turnos_cosmetica():
    for i in range(1,1000):
        yield f'C-{i}'

p = turnos_perfumeria()
f = turnos_farmacia()
c = turnos_cosmetica()

def decorador (campo):

    print('Saludos, su turno es:')
    if campo == 'P':
        print(next(p))
    elif campo == 'F':
        print(next(f))
    if campo == 'C':
        print(next(c))
    print('Espere ser atentido.')