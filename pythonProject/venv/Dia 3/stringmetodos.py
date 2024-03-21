texto = "Este es el texto de Federico"

resultado = texto

print(resultado)
print(resultado.upper())#Convierte en mayuscula
print(resultado[2].upper())#Convierte en minuscula la letra indicada
print(resultado.lower())#Convierte en minuscula
print(resultado[0].lower())
print(resultado.split())#Convierte el texto en una lista de palabras por espacios
print(resultado.split("t"))#Divide el texto por el caracter indicado
print(resultado.replace("Federico","Alex"))#Reemplaza texto
print(resultado.replace("e","a"))#Reemplaza texto
print("Find", resultado.find("s"))#Lo mismo que index
#Si no encuentra el caracter dentro del string, no nos da error sino que devuelve -1


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])#Une los elementos de una lista, y los divide con el caracter indicado
f = "-".join([a,b,c,d])#Une los elementos de una lista, y los divide con el caracter indicado
print(e)
print(f)