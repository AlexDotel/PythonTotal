# ZIP
# Conjuga dos o mas listas en una sola, pueden ser tuples, diccionarios y demas
# Siempre llega hasta la lista mas corta, como en el ejemplo de abajo
# las uniria hasta Michael, y el 55 quedaria en el aire.

# Para  ser mostrados deben ser casteados en una lista, como se ve en la linea 12

nombre = ['Alex','Cinthia','Emily','Michael']
edades = [27,28,6,3,80]
paises = ['Mexico','Madrid','Andalucia','Segovia']

comb = list(zip(nombre,edades,paises))
print(comb)

# Ejemplo de uso:
for nombre, edad, ciudad in comb:
    print(f"{nombre} tiene {edad} anos, y vive en {ciudad}")