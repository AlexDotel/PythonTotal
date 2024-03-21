mset = set([1,2,3,4,2,(2,2,3),2,2,3,5])
print(type(mset))
print('mset', mset)

oset = {5,4,3,2,1}
print(type(oset))
print('oset', oset)

print('Longitud', len(mset))
print('Esta el dos?', 2 in mset)

# print(mset[0])    NO SE PUEDE
# set[0] = 1        NO SE PUEDE
# No admite listas
# Si admite tuples, porque son inmutables
# No respeta orden, no tiene indices


s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
# Aqui unimos dos sets, como ves en la impresion no se repiten los elementos.

s3.add(6)
# Podemos agregar valores
s3.add(2)
# Este valor no lo agregara porque esta repetido
s3.remove(3)
# Eliminamos algun elemento con remove
s3.discard(3)
# Descartar es igual que remove, pero si el solicitado no existe no da error.
s3.pop()
# Se puede almacenar => concurso = s3.pop()
# Elimina un elemento aleatorio, porque en este caso no tiene ningun orden
s3.clear()
# Vaciar el set
print(s3)