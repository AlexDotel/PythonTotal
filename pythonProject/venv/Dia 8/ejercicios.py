def funcion():
    num = 0
    while True:
        num += 1
        yield num

def multiplos_siete():
    num = 0
    while True:
        num += 1
        yield num * 7

generador = multiplos_siete()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


def restando_vidas():
    vidas = 3
    while vidas > 0:
        if vidas > 1:
            yield f'Te quedan {vidas} vidas'
        elif vidas == 1:
            yield f'Te queda {vidas} vida'
        vidas -= 1
    yield "Game Over"

perder_vida = restando_vidas()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
