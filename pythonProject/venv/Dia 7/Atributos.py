class Pajaro:

    # def __init__(self, parametro):
    #     # CONSTRUCTOR
    #    self.atributo = parametro
    #    #El parametro debe ser igual, es buena practica que los dos sean del mismo nombre

    alas = True
    #Atributos de clase para todas las instancias de las clases

    def __init__(self, color, especie):  # CONSTRUCTOR
        self.color = color
        self.especie = especie


loro = Pajaro('Verde', 'Loro')
# Ahora exije un argumento color.

print(f'Mi pajaro es de color {loro.color}, de la especie {loro.especie}')
#Aqui llamamos el color del pajaro.
print(loro.alas)


class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')

print(cubo_rojo.color)


class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)

print(harry_potter.especie, harry_potter.edad, harry_potter.magico)