class Pajaro:

    alas = True

    def __init__(self, color, especie):  # CONSTRUCTOR
        self.color = color
        self.especie = especie


    #   METODOS DE INSTANCIA
    #   Pueden modificar los atributos de instancia, y el estado de clase.

    def piar(self):
        print(f'Pio, mio color es {self.color}.')

    def volar(self, metros):
        print(f'El pajaro volo {metros} metros')
        self.piar()
        # Se pueden llamar otros metodos de la instancia

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}.')
        # Este metodo puede cambiar propiedad de la instancia

    #   METODOS DE CLASE
    #   No necesitan instancia para ejecutarse desde fuera, llamando a la clase basta
    #   Por eso tampoco pueden acceder a los atributos de instancia dentro del .self
    #   Se declaran con un decorador @classmethod, como parametro lleva cls en vez de self

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos.')
        cls.alas = False
        print(Pajaro.alas) # Se pueden modificar atributos de la clase

    #   METODOS ESTATICOS
    #   Llevan el decorador @staticmethod
    #   NO accede ni modifica los argumentos de clase o de metodo.

    @staticmethod
    def mirar():
        print('El pajaro mira')
        # self.color = 'rojo' DA ERROR
        # cls.alas = False    DA ERROR


piolin = Pajaro('amarillo', 'canario')


Pajaro.poner_huevos(2)

