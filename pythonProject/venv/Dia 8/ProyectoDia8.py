import modulosProyecto

def preguntar ():

    print('Bienvenido.')

    while True:
        print('''[P] Perfumeria?
[F] Farmacia
[C] Cosmetica''')

        try:
            campo = input('Elija su campo').upper()
            ['P', 'F', 'C'].index(campo)
            # Si campo tiene algo distinto, da error.
        except ValueError:
            print('Eleccion invalida.')
        else:
            break

    modulosProyecto.decorador(campo)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('Quieres otro turno?').upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print('Eleccion invalida.')
        else:
            if (otro_turno == 'N'):
                print('Gracias por su visita.')
                break

inicio()



