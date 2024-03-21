lista = ["a","b","c"]
otra = ['hola', 2, 1.5]

final = lista+otra

print(type(lista))
print(len(lista))
print(otra[0:3])
print(lista+otra)


final[0] = "alpha" #Reemplazar un elemento

print(final)

final.append(12)
#Agregar un elemento

final.pop()
#Elimina el ultimo elemento

eliminado = final.pop()
#Almacena el elemento elminado

print(final)
print(eliminado)



#Ordenar Lista:
lista = ['g','a','n','w','t','a','b','z']

lista.sort()
print("Lista Ordenada: ", lista)
# Ordena la lista en orden alfabetico,
# no devuelve nada, solo ordena la lista.

lista.reverse()
print("Lista Desordenada: ", lista)
# Ordena la lista alreverso del alfabeto,
# no devuelve nada, solo ordena la lista.
