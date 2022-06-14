import pygame
import random
import math
from pygame import mixer
# Inicializar Pygame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono
pygame.display.set_caption("Juegazo papu")
icono = pygame.image.load("cohete.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

mixer.music.load("MusicaFondo.mp3")
mixer.music.play(-1)
# Jugador

img_player = pygame.image.load("nave-espacial.png" )
img_player = pygame.transform.scale(img_player, (64,64))

# Variables jugador

jugador_x = 368
jugador_y = 520
jugador_x_cambio = 0

# Variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 4

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png" ))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(30)

# Variables de la bala
img_bala = pygame.image.load("bala.png" )
bala_x = 0
bala_y = 520
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False

# Puntaje

puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# texto final

fuente_final = pygame.font.Font('freesansbold.ttf', 100)

def texto_final():
    mi_fuente_final = fuente.render("JUEGO TERMINADO" , True , (255,255,255))
    pantalla.blit(mi_fuente_final,(300,200))
# Funciones


def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x,y))


def jugador(x,y):
    pantalla.blit(img_player , (x,y))


def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene] , (x,y))


def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10))


def colisiones(x_1,y_1 ,x_2 ,y_2):

    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_2- y_1,2))
    if distancia < 27:
        return True
    else:
        return False

# Loop del juego

ejecucion = True

while ejecucion:
    # Color pantalla

    pantalla.blit(fondo,(0,0))
    # iterar eventos
    for evento in pygame.event.get():
        # Evento cerrar
        if evento.type == pygame.QUIT:
            ejecucion = False

        # Controles de la nave

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
               jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)

        # Si se solto las flachas
        if evento.type  == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
               jugador_x_cambio = 0

    # Actualizacion de la panta y el jugador

    jugador_x += jugador_x_cambio

    # Limites

    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar al enemigo
    for e in range(cantidad_enemigos):

        #fin del juego
        if enemigo_y[e]>500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]

        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        # Colision
        colision = colisiones(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("Golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] =random.randint(0, 736)
            enemigo_y[e] =random.randint(50, 200)
        enemigo(enemigo_x[e], enemigo_y[e],e)
    # Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y-= bala_y_cambio

    # Actualizando
    mostrar_puntaje(texto_x,texto_y)
    jugador(jugador_x, jugador_y)
    pygame.display.update()