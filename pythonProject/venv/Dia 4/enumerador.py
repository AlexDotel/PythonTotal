# ENUMERATE

# Sin enumerate
lista = ["a","b","c"]
indice = 0

for item in lista:
    print(indice,item)
    indice+=1

# Con enumerate
lista = ["a","b","c"]

for item in enumerate(lista):
    print(item)

# Con enumerate para que quede exactamente igual
lista = ["a","b","c"]

for indice, item in enumerate(lista):
    print(indice, item)

# Con enumerate y con range
for indice, item in enumerate(range(11,20)):
    print(indice, item)

# Convertir lista en tuple
lista = ["a","b","c"]
mtuple = list(enumerate(lista))
print(mtuple)
print(mtuple[1][0])