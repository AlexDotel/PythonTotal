import re

texto = 'Si necesitas ayuda llama al 809-555-5555 y recibiras ayuda rapidamente'

patron = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
# Nos da la ubicacion
print(busqueda.start())
# Nos da la ubicacion de inicio
print(busqueda.end())
# Nos da la ubicacion final

busqueda = re.findall(patron, texto)
print(busqueda)
# Nos da todas las coincidencias

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
# Forma de iterar correctamente


texto = 'Llama al 809-752-9383'

# patron = r'\d\d\d-\d\d\d-\d\d\d\d' FORMA LARGA
patron = r'\d{3}-\d{3}-\d{4}'
# Encontrara cualquier numero con este patron
# Recordando que la d =  digito numerico.
busqueda = re.search(patron, texto)
print(busqueda.group())


patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
busqueda = re.search(patron, texto)
print(busqueda.group())
print(busqueda.group(1))
# Usando compile





# Uso practico clave con requisitos:
#
# clave = input('Clave: ')
patron = r'\D{1}\w{7}'
# chequear = re.search(patron, clave)
# print(chequear)


#

texto = '4No atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes', texto)
# Buscar mas de uno.
print(buscar)

buscar = re.search(r'...demos...', texto)
# Buscar lo que pusimos e incluir los caracteres donde pusimos los puntos.
print(buscar)

buscar = re.search(r'^\D', texto)
# Este signo invierte la solicitud, escomo poner !
# Nos devuelve en este caso si existe un NO DIGITO, al principio del texto.
print(buscar)

buscar = re.search(r'\D$', texto)
# Nos devuelve en este caso si existe un NO DIGITO, al final del texto.
print(buscar)

buscar = re.findall(r'[^\s]', texto)
# Ubica todos los caracteres que NO sean espacios vacios, por usar corchetes.
print(buscar)

buscar = re.findall(r'[^\s]+', texto)
# Ubica todos los caracteres que NO sean espacios vacios, CONSECUTIVAMENTE.
print(''.join(buscar))
