# -*- coding: latin1 -*-

import pygame, sys
from pygame.locals import *

pygame.init()

janela=pygame.display.set_mode((300,300), 0,32)
pygame.display.set_caption("Jogo da velha")



pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()