from pathlib import Path

base = Path.home()
guia = Path('barcelona','sagrada_familia')
# Convierte los argumentos de texto recibidos a una ruta

completa = Path(base,Path('Europa', 'Espana'),Path('barcelona','sagrada_familia'),'centro_museo')
guia_2 = guia.with_name('pedrera.txt')
# Concatenamos un archivo al final de la ruta, a una nueva ruta

print('Mi Base: ',base)
print(completa)
print('Guia 2',guia_2)

print(guia.parent)
# Devuelve el antecesor mas inmediato de dicha ruta
print(guia.parent.parent)
# Podemos ir retrocediendo en la ruta subiendo de niveles mientras mas se use parent







