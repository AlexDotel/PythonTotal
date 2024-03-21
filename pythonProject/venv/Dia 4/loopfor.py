# ITERANDO LISTAS

nombres = ['Alex', 'Manuel', 'Cinthia', 'Antonia','Emily', 'Michael']

for elemento in nombres:
    # print("Hola",elemento)
    if elemento.startswith('A'):
        numero = nombres.index(elemento)+1
        print(f"{numero}. {elemento}")
print("\n")

lista = [[1,2],[3,4],[5,6]]

for objeto in lista:
    print(objeto)
print("\n")

for a,b in lista:
    # print(f"{a} {b}")
    print(a)
    print(b)
print("\n")

# ITEANDO DICCIONARIOS

dic = {'c1':'a','c2':'b','c3':'c'}
for item in dic:
    print(item)
    #En este caso se imprimen las claves.
print("\n")

for item in dic.values():
    print(item)
    # En este caso se imprimen los valores.
print("\n")

for item in dic.items():
    print(item)
    # En este caso se imprimen los objetos completos.
