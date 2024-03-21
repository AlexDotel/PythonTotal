texto = "Esta es una prueba"
resultado = texto.index("n")

print(resultado)

print(texto.index("a"))
#Conocer el indice de un caracter, si la cadena de texto dentro de la variable
#no almacena dicho caracter, entonces da un error.
#Es susceptible a mayusculas
#Si el caracter esta repetido, nos da el indice su primera aparicion


print(texto.index("a",5))
#En este caso lo mismo pero empieza a buscar a partir del indice indicado


print(texto.index("a",5,11))
#En este caso lo mismo pero tambien limitamos la busqueda hasta donde queramos

print(texto.rindex("a"))
#Igual que .index pero al revez, empieza a buscar desde atras

print(texto[0])
#Llama el caracter dentro de un indice

print(texto[-1])
#Llama los caracteres en orden inverso

print(texto.index("prueba"))
#En caso de una palabra, la ubica y devuelve el indice donde comienza la misma

