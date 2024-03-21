class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('Jajaja')

    def hablar(self):
        print('Que tal?')

class Hijo(Padre, Madre):
    pass
# Hijo hereda de padre y madre, el orden es importante
# Elegira el metodo del padre que fue declarado primero
# entre dos metodos que coincidan en ambos padres

class Nieto(Hijo):
    pass
# Nieto, hereda todo lo que hereda hijo, de padre y madre.
# Si nieto tuviese un metodo que choque con el de hijo, padre
# o madre, entonces usaria el metodo de nieto, porque va buscando
# de abajo hacia arriba.

mi_nieto = Nieto()

mi_nieto.hablar()
# Aqui confirmamos que usa el hablar de padre, porque hijo hereda
# de padre, primero que de madre, el orden es crucial.

mi_nieto.reir()
# Metodo heredado de madre

print(Nieto.__mro__)
# Aqui con __mro__, vemos el orden de herencia establecido en este objeto.