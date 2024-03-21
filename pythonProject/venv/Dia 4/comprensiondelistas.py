# COMPRENSION DE LISTAS

# MODO BASICO
palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

# MODO INTELIGENTE
palabra = 'python'
lista2 = [item for item in palabra]
print (lista2)

# MODO INTELIGENTE
lista2 = [letra for letra in 'python']
print (lista2)

# CON NUMEROS
numeros = [num for num in range(1,11)]
print(numeros)

# CON NUMEROS Y OPERACIONES
numeros = [num / 2 for num in range(1,11)]
print(numeros)

# CON NUMEROS Y OPERACIONES Y CONDICIONES IF
numeros = [num / 2 for num in range(1,11) if num % 2 == 0]
print(numeros)

# CON NUMEROS Y OPERACIONES Y CONDICIONES IF Y ELSE
numeros = [num / 2 if num % 2 == 0 else 'no' for num in range(1,11) ]
print(numeros)
# En este caso se pasa delante


# Ejemplo

pies = list(range(10,51,10))
print(pies)
metros = [m * 3.281 for m in pies]
print(metros)