import pygame as p
import random

# Inicializando pygame
p.init()

# Creando pantalla
pantalla = p.display.set_mode((800, 600))

# Titulo, fondo e Icono
p.display.set_caption('Invasion Espacial')
icono = p.image.load('ovni.png')
p.display.set_icon(icono)
fondo = p.image.load('fondo.jpg')

# Variables Jugador
rocket_img = p.image.load('rocket.png')
rocket_x = 368
rocket_y = 500
rocket_x_cambio = 0

# Variables Enemigo
enemy_img = p.image.load('enemy.png')
enemy_x = random.randint(0,736)
enemy_y = random.randint(50,200)
enemy_x_cambio = 0.3
enemy_y_cambio = 50

# Variables Bala
bala_img = p.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# Funcion Jugador
def rocket(x,y):
    pantalla.blit(rocket_img, (x, y))

# Funcion Enemigo
def enemy(x,y):
    pantalla.blit(enemy_img, (x, y))

# Funcion Enemigo
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala_img, (x + 16, x + 10))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Pintando la pantalla o imagen de fondo
    # pantalla.fill((153,153,255))
    pantalla.blit(fondo, (0,0))

    # Iterar eventos
    for evento in p.event.get():

        # Evento Cerrar Programa
        if evento.type == p.QUIT:
            se_ejecuta = False

        # Evento Presionar Teclas
        if evento.type == p.KEYDOWN:
            if evento.key == p.K_LEFT:
                rocket_x_cambio = -1
            if evento.key == p.K_RIGHT:
                rocket_x_cambio = 1
            if evento.key == p.K_SPACE:
                disparar_bala(rocket_x, bala_y)

        # Evento Soltar Flechas
        if evento.type == p.KEYUP:
            if evento.key == p.K_LEFT or evento.key == p.K_RIGHT:
                rocket_x_cambio = 0

    # Modificar ubicacion rocket
    rocket_x += rocket_x_cambio

    # Limitar movimiento a bordes rocket
    if rocket_x <= 0:
        rocket_x = 0
    if rocket_x >= 736:
        rocket_x = 736

    # Modificar ubicacion enemy
    enemy_x += enemy_x_cambio

    # Limitar movimiento a bordes enemy
    if enemy_x <= 0:
        enemy_x_cambio = 0.3
        enemy_y += enemy_y_cambio
    if enemy_x >= 736:
        enemy_x_cambio = -0.3
        enemy_y += enemy_y_cambio

    # Movimento Bala
    if bala_visible:
        disparar_bala(rocket_x, bala_y)
        bala_y = bala_y - bala_y_cambio

    rocket(rocket_x, rocket_y)
    enemy(enemy_x, enemy_y)

    # Actualizar
    p.display.update()