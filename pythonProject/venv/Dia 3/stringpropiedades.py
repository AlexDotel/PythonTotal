nombre = "carina"
#nombre[0] = "K"
#No se puede cambiar solo reescribir

nombre = "Karina"
apellido = " Gomez"

print(nombre)
print(nombre + apellido)
print(nombre * 2)
#Se puede multiplicar

poema = """Mil pequenos peces blancos
como si hirviera el color del agua"""
#Para soportar saltos de linea podemos usar comillas triples

print(poema)

print("agua" in poema)
#Confirmar la existencia de un texto dentro de la variable
print("agua" not in poema)
#Negar la existencia de un texto dentro de la variable

print(len(poema))
#Saber la longitud del contenido