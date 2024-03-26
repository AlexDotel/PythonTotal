import pygame as p

# Inicializando pygame
p.init()

# Creando pantalla
pantalla = p.display.set_mode((800, 600))

# Titulo e Icono
p.display.set_caption('Invasion Espacial')
icono = p.image.load('ovni.png')
p.display.set_icon(icono)

# Variables Jugador
rocket_img = p.image.load('rocket.png')
rocket_x = 368
rocket_y = 536
rocket_x_cambio = 0

# Funcion Jugadore
def rocket(x,y):
    pantalla.blit(rocket_img, (x, y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Pintando la pantalla
    pantalla.fill((153,153,255))

    # Iterar eventos
    for evento in p.event.get():

        # Evento Cerrar Programa
        if evento.type == p.QUIT:
            se_ejecuta = False

        # Evento Presionar Flechas
        if evento.type == p.KEYDOWN:
            if evento.key == p.K_LEFT:
                rocket_x_cambio = -0.3
            if evento.key == p.K_RIGHT:
                rocket_x_cambio = 0.3

        # Evento Soltar Flechas
        if evento.type == p.KEYUP:
            if evento.key == p.K_LEFT or evento.key == p.K_RIGHT:
                rocket_x_cambio = 0

    # Modificar ubicacion
    rocket_x += rocket_x_cambio

    # Limitar movimiento a bordes
    if rocket_x <= 0:
        rocket_x = 0
    if rocket_x >= 736:
        rocket_x = 736

    rocket(rocket_x, rocket_y)

    # Actualizar
    p.display.update()