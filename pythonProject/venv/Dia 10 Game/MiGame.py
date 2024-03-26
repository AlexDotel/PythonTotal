import pygame as p

# Inicializando pygame
p.init()

# Creando pantalla
pantalla = p.display.set_mode((800, 600))

# Titulo e Icono
p.display.set_caption('Invasion Espacial')
icono = p.image.load('ovni.png')
p.display.set_icon(icono)

# Jugador
rocket_img = p.image.load('rocket.png')
rocket_x = 368
rocket_y = 536

def rocket():
    pantalla.blit(rocket_img, (rocket_x, rocket_y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Pintando la pantalla
    pantalla.fill((236,236,236))
    for evento in p.event.get():
        if evento.type == p.QUIT:
            se_ejecuta = False
    rocket()

    p.display.update()