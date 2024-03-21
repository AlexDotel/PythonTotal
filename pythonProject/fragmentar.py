texto = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
framento = texto[2:10]
#Selecciona una serie de caracteres

print(framento)

print(texto[2:])
#En caso de no poner nada luego de los dos puntos, los selecciona todos hasta el final.


print(texto[:5])
#En caso de no poner nada antes de los dos puntos, los selecciona todos desde el inicio.

print(texto[2:10:2])
#Aqui lo mismo, pero salteamos cada 2 caracteres, como indicamos en el 3er parametro