def suma(**kwargs):
    print(type(kwargs))

suma(x = 2, y = 5, z = 2)

# Prueba de como usar los KWARGS
def prueba (n1, n2, *args, **kwargs):
    print(n1)
    print(n2)
    for arg in args:
        print(arg)
    for name,item in kwargs.items():
        print(name,"=",item)

prueba(12,24,100,200,300, x='1', y='2', z='3')






def lista_atributos(**atributos):
    lista = []
    for clave,obj in atributos.items():
        lista.append(obj)
    return lista
print('\n')
print(lista_atributos( x='1', y='2', z='3'))



def describir_persona(nombre,**argumentos):
    print(f'Características de {nombre}:')
    for key,arg in argumentos.items():
        print(f'{key}: {arg}')
describir_persona("María", color_ojos="azules", color_pelo="rubio")
