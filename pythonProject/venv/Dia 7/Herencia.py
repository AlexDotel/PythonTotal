class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido.')

class Pajaro(Animal):
    pass

print(f'Clase heredada: {Pajaro.__bases__}')
print(f'Clases herederas: {Animal.__subclasses__()}')

# Asi una clase hereda otra, poniendo la heredad entre parentesis
# Haciendo que todos los atributos de ANIMAL consten dentro de pajaro.

piolin = Pajaro(2, 'Amarillo')
print(piolin.color)