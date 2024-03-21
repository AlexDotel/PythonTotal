# MIN MAX
# Siver para discriminar el menor o mayor de una lista
# Tambien ordena por alfabeto, priorizando las mayusculas

menor = min(1,2,3,4)
print(menor)
mayor = max(1,2,3,4)
print(mayor)
print('\n')


lista = [1,23,45,67,887,543,23213,45345,23133]
print(f'El mejor es {min(lista)}, y el maximo es {max(lista)}')
print('\n')

nombres = ['juan','pablo','alicia','zeri']
print(min(nombres))
print(max(nombres))
print('\n')

nombre = 'Alex'
print(min(nombre))
print('\n')

nombre = 'alEx'
print(min(nombre))
print('\n')
# Prioriza Mayusculas y luego el afabeto

dicci = {'c1':'Zeri', 'c2':'Alba'}
print(min(dicci.values()))
# en caso de un diccionario discriminara la clave, no el valor.

