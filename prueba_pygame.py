import pygame

pygame.init()
pygame.display.set_mode((1500, 750))
pygame.display.set_caption("Mi primer juego con Pygame")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()