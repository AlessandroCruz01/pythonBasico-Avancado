import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
    tela.fill((0,0,0))
    pygame.display.flip()