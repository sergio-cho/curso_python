import pygame
# Inicializar Pygame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e icono
pygame.display.set_caption("Juegazo papu")
icono = pygame.image.load("cohete.png")
pygame.display.set_icon(icono)

#Jugador
img_player = pygame.image.load("nave-espacial.png")

jugador_x = 0
judador_y = 0

def jugador():
    pantalla.blit(img_player((jugador_x,judador_y)))

# Loop del juego
ejecucion = True

while ejecucion:
    #COlor pantalla
    pantalla.fill((3, 252, 127))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecucion = False

    jugador()
    pygame.display.update()