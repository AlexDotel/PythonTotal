from os import system

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'''Cliente: {self.nombre} {self.apellido},
        Numero de cuenta: {self.numero_cuenta}
        Balance disponible: {self.balance}'''

    def depositar(self):
        print(f'Balance Actual: {self.balance} EUR')
        deposito = int(input('Cantidad a depositar: '))
        self.balance += deposito
        print(f'Ahora tiene {self.balance} EUR')

    def retirar(self):
        print(f'Balance Actual: {self.balance} EUR')
        retiro = self.balance + 1
        while retiro > self.balance:
            retiro = int(input('Cantidad a retirar: '))
            if retiro < self.balance:
                self.balance -= retiro
                print(f"Has retirado: {retiro} euros, te quedan {self.balance}")
            else:
                print('No tienes tanto dinero')

cliente = Cliente('Josue', 'Reyes', 12, 100)

def saludar():
    print('Bienvenido al banco del pueblo.')
    respondio = False
    while respondio == False:
        desicion = str(input('¿Desea REGISTRARSE? S/N'))
        if desicion.upper() == 'S':
            registrarse()
            respondio = True
        elif desicion.upper() == 'N':
            system('cls')
            print('Hasta luego, gracias por usar nuestro recetario')
            respondio = True
            exit()

def registrarse():
    print('Iniciemos con el registro')
    nombre = str(input('Nombre: '))
    apellido = str(input('Apellido: '))
    numero_cuenta = 1122329930
    balance = str(input('Deposito Inicial: '))

    mi_cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    operaciones(cliente)

def operaciones(cliente):
    print('Operaciones', cliente)
    operacion = 0
    rango = range(4)
    while (operacion not in rango or operacion == 0):
        print(f'''¿Que quieres hacer?
        1. Depositar Dinero
        2. Retirar Dinero
        3. Terminar programa
        ''')
        operacion = int(input('Elige una opcion: '))
    if operacion == 1:
        cliente.depositar()
        fin_programa(cliente)
    if operacion == 2:
        cliente.retirar()
        fin_programa(cliente)
    if operacion == 3:
        print('Gracias por preferir el banco del pueblo, hasta pronto.')
        exit()

def fin_programa(cliente):
    # FINALIZANDO O VOLVIENDO
    respondio = False
    while respondio == False:
        seguir = str(input('¿Desea realizar otra operacion? S/N'))
        if seguir.upper() == 'S':
            system('cls')
            respondio = True
            operaciones(cliente)
        elif seguir.upper() == 'N':
            system('cls')
            print('Hasta luego, gracias.')
            respondio = True
            break

def programa():
    saludar()

programa()
