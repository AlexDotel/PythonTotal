class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido.')

class Pajaro(Animal):

    # Si creamos un init, con atributos nuevos no hay problema, pero debemos
    # declarar los atributos heredados obligatoriamente.

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    # IMPORTANTE: Existe una forma mas corta de declarar los atributos
    # heredados, es con un metodo super() __init__, en vez de la forma
    # tradicional que nos exige hacerlo linea por linea.


    # METODO TRADICIONAL
        # self.edad = edad
        # self.color = color
        # self.altura_vuelo = altura_vuelo



    def hablar(self):
        print('Pio')
    # Si creamos un metodo heredado, lo sobreescribe

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros.')
    # Podemos crear un metodo nuevo o mas

piolin = Pajaro(3, 'Amarillo', 20)
mi_animal = Animal(5, 'negro')

piolin.nacer()
