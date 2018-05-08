import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

# Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

# Rafraîchissement de l'écran
pygame.display.flip()

# BOUCLE INFINIE
clock = pygame.time.Clock()
continuer = 1
while continuer:
    clock.tick(60) # Pas plus de 60 FPS
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == K_DOWN:
                position_perso = position_perso.move(0, 10)
            if event.key == K_UP:
                position_perso = position_perso.move(0, -10)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(10, 0)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-10, 0)
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:  # Uniquement le clic gauche
                position_perso.x, position_perso.y = pygame.mouse.get_pos()
                position_perso.x = position_perso.x - 42
                position_perso.y = position_perso.y - 42

    # Re-collage
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()
