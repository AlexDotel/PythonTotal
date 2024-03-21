class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre, 'dice muuu')

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre, 'dice beee')

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

vaca1.hablar()
oveja1.hablar()
# Aunque el metodo es igual, funciona bien porque
# son clases diferentes gracias al polimorfismo

animales = [vaca1, oveja1]

for i in animales:
    i.hablar()
    # Aunque son metodos distintos, se llaman igual
    # Asi que en la iteracion, funcionan cada uno.

def animal_habla(animal):
    animal.hablar()
animal_habla(vaca1)
# El metodo es distintio, pero se llama igual
# El polimorfismo lo hace posible.