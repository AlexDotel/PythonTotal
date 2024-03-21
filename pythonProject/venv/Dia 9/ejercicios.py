from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)

lista_ciudades.append('Santo Domingo')
lista_ciudades.appendleft('Barahona')
print(lista_ciudades)