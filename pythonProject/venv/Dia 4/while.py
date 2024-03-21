# While

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas.")
    monedas -= 1 #monedas = monedas -1
else:
    print("Se acabaron las monedas.")


# Ejemplo 2
# Fuera del control del programador

respuesta = "s"

while respuesta != "n":
    if respuesta == 's':
        respuesta = input("Quieres seguir S/N: ").lower()
    else:
        print("""Introduce S o N""")
        respuesta = input("Quieres seguir S/N: ").lower()
else:
    print("Gracias, no seguiremos")


# RECORDAR
# break, pass, continue
# break:    Sirve para Terminar el programa cuando se da una condicion
# pass:     Sirve para dejar una linea de codigo inconclusa como un while sin condicion
# continue: Sirve para saltar una linea de codigo


numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero-=1
    elif numero == 0:
        print(numero)
        numero-=1
    else:
        numero-=1