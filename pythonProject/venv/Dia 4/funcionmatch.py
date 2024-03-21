# En otros lenguajes esto es Switch:

serie = 'N-02'

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("iPhone")
    case _:
        print("Desconocido")


        
#Ejemplo Avanzado:

cliente = {'nombre':'federico',
           'edad':'45',
           'ocupacion':'instructor'}

pelicula = {'titulo':'matrix',
            'ficha_tecnica':{'protagonista':'keanu reeves',
                             'director':'Lana y Lilly Watchowski'}}

elementos = [cliente, pelicula, 'libro']


for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad': edad,
              'ocupacion':ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo':titulo,
              'ficha_tecnica':{'protagonista':protagonista,
                               'director':director}}:
            print('Es una pelicula')
            print(titulo, director, protagonista)
        case _:
            print('No se que es esto')