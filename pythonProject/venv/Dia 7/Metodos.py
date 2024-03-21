class Pajaro:

    alas = True

    def __init__(self, color, especie):  # CONSTRUCTOR
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'Pio, mio color es {self.color}.')
        # El parametro 'self' es obligatorio en metodos de clases.

        # Este envia la informacion de todos los atributos
        # que contiene clase a el metodo en cuestion.

        # Al momento de llamar cualquier atributo
        # hemos de hacerlo usando 'self.' delante

    def volar(self, metros):
        print(f'El pajaro volo {metros} metros')
        # Se pueden pedir otros parametros


piolin = Pajaro('amarillo', 'canario')
piolin.piar() #Imprimira 'Pio.'
piolin.volar('50')

