from collections import Counter

numeros = [8,9,3,5,2,3,2,2,4,3,3,2,3,4,2,3,4,3,3,3,4,2]

print(Counter(numeros))
# Crea un diccionario contando los numeros las veces que se repite.

print(Counter('misisipi'))
# Funciona con cadenas de texto.

print(Counter('Al agua Pato.'))
# Funciona con oraciones y discrimina mayusculas y minuscula.


print('')

serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3])
print(serie)
print(serie.most_common())
# Devuelve tuplas ordenando los caracteres mas comunines.
print(serie.most_common(1))
# Solo muestra el que mas aparece.
print(serie.most_common(2))
# Solo muestra los dos que mas aparecen.
print(list(serie))
# Devuelve una lista con los elementos de mi serie.

