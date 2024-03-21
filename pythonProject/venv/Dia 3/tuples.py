# Tuples
# Ocupan menos espacio, sin inmutables

mi_tuple = (1,2,3,4)

t = (5,5.6,'ff',)
# Pueden tener valores de diferentes tipos

print(type(mi_tuple))
print(mi_tuple)
print(mi_tuple[0])
print(mi_tuple[-2])

tuple2 = (1,2,(2.5,3,3.5),4)
# Se pueden anidar, es decir crear tuples, dentro de otros
print(tuple2[2])
print(tuple2[2][1])

tuple3 = list(tuple2)
print(type(tuple3))
print(tuple3)
# Se puede castear a lista

tuple3 = tuple(tuple3)
print(type(tuple3))
print(tuple3)
# Y nuevamente de lista se puede castear a tuple



ejes = (1,2,3,1)
# x,y,z = ejes
# print(x,y,z)
# Se autoasignan valores al x,y,z tambien se puede hacer en las listas
# Esto siempre y cuando tengan la misma cantidad de elementos ni mas ni menos

print(ejes.count(1))
# Cuenta cuantas veces aparece un valor dentro de la lista o tuple.

print(ejes.index(2))
# Nos indica en que indice esta el valor indicado