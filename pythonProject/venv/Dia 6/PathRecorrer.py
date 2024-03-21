from pathlib import Path

europa_guia = Path(Path.home(), 'Europa')

for txt in europa_guia.glob('*.txt'):
    # De esta forma recorremos todos los archivos de texto dentro de europa
    print(txt)

print('...')

for txt in europa_guia.glob('*'):
    # De esta forma recorremos todas las carpetas y todos los archivos de texto dentro de europa
    print('carpetas:',txt)


print('...')


europa_guia = Path('Europa','España','Barcelona', 'Sagrada_Familia' )

en_europa = europa_guia.relative_to(Path('Europa'))
# Se usa este modo relative_to para acceder a una carpeta, desde una ruta predefinida
en_espania = europa_guia.relative_to(Path('Europa', 'España'))

print('En europa:',en_europa)
print('En espania:',en_espania)
