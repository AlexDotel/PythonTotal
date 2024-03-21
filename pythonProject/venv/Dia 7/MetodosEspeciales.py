class CD:

    def __init__(self, autor, titulo, cantidad_canciones):
        self.autor = autor
        self.titulo = titulo
        self.cantidad_canciones = cantidad_canciones

    def __str__(self):
        return f'Album: {self.titulo}, de {self.autor}'
    # En este caso al imprimir cualquier instancia de esta clase
    # se imprimira de la forma que hemos establecido en el metodo
    # especial str.

    def __len__(self):
        return self.cantidad_canciones
    # Aqui por ejemplo al llamar len en vez de dar error retorna
    # la cancidad de canciones.

    def __del__(self):
        print('Se ha eliminado el CD')
    # Aqui imprimimos un mensaje cuando se elimine alguna instancia
    # de nuestra clase usando el metodo especial del, mismamente
    # podriamos hacer que no se eliminara, sino que se diera otra accion



mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)
print(len(mi_cd))
del mi_cd