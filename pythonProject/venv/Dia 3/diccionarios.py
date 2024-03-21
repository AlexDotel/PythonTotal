# diccionario = {'c1':'valor1', 'c2':'valor2'}
#
# print(diccionario)
#
# print(diccionario['c1'])
# # Llamar un valor
#
#


# cliente = {'nombre':'Juan', 'apellido':'Reyes', 'edad': 45, 'talla':1.76}
# consulta = (cliente['talla'])
#
# print(consulta)


dic = {'c1':55, 'c2':[10,20,30], 'c3':{'c1':100, 'c2':200}}

print(dic['c2'][1])
print(dic['c3']['c2'])
# Buscar dentro de un diccionario dentro de un diccionario.

dicc = {'c1':['a','b','c'], 'c2':['d','e','f']}
print('\n')
print(dicc['c2'][1].upper())
# Buscar dentro de una lista almacenada en un diccionario

diccc = {1:'a', 2:'b'}

diccc[3] = 'c'
print(diccc)
# Agregar elemento a un diccionario

diccc[2] = 'B'
print(diccc)
# Reemplazar item en un diccionario

print(diccc.keys())
# Conocer las claves de un diccionario

print(diccc.values())
# Conocer los valores de un diccionario

print(diccc.items())
# Conocer todo lo que hay en un diccionario