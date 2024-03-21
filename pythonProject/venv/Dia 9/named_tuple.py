from collections import namedtuple

mi_tupla = (100,200,2)

print(mi_tupla[1])
# En una tupla larga podemos olvidarnos de los valores.

Persona = namedtuple('Persona', ['nombre','altura','peso'])
# Sin embargo con namedtuple podemos nombrar cada valor, en un objeto.

ariel = Persona('Ariel', 170, 89)
# Crear una instancia de ese objeto namedtuple para...

print(ariel.altura)
# Luego llamar dicho valor por su nombre.
print(ariel[1])
# O llamarlo convencionalmente.