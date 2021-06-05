# -*- coding: UTF-8 -*-

#IMPORTAÇÃO DO PYGAME
import pygame , sys
from pygame.locals import *


#INICIA O PYGAME
pygame.init()


#INICIA A JANELA DO PYGAME
janelaSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption("Olá mundo")

#INICIA AS CORES UTILIZADAS
BLACK = (0,0,0) #PRETO
WHITE = (255,255,255) #BRANCO
RED = (255,0,0) #VERMELHO
GREEN = (0,255,0) #VERDE
BLUE = (0,0,255) #AZUL


#INICIA AS FONTES
Fonte = pygame.font.SysFont(None,48)

#INICIA O TEXTO
# texto = Fonte.render("Ola mundo", True, WHITE,GREEN)
# textoReact = texto.get_rect()
# textoReact.centerx = janelaSurface.get_rect().centerx
# textoReact.centery = janelaSurface.get_rect().centery

#DESENHA FUNDO BRANCO
janelaSurface.fill(WHITE)

#DESENHA UM POLIGONO VERDE
# pygame.draw.polygon(janelaSurface, GREEN, ((146,0),(291,106),(236,277),(56,277),(0,106)))

#DESENHA ALGUMAS LINHAS AZUIS NA SUPERFICIE
pygame.draw.line(janelaSurface, BLUE, (60,60), (120,60), 4)
pygame.draw.line(janelaSurface, BLUE, (120,160), (60,120))
pygame.draw.line(janelaSurface, BLUE, (140,200), (120,60), 4)

#DESENHA UM CIRCULO AZUL NA TELA
pygame.draw.circle(janelaSurface, BLUE, (300,50), 20,0)

#DESENHAR UMA ELIPSE VERMELHA NO FUNDO
pygame.draw.ellipse(janelaSurface, RED, (300, 250, 40, 80), 1)


#DESENHA A JANELA NA TELA
pygame.display.update()

#RODA O LOOP DO PROGRAMA
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()




screen = pygame.display.set_mode((600,600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
    screen.fill((0,0,0))





    pygame.display.flip()
