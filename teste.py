from random import randint
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1220,720))
clock = pygame.time.Clock()

ratu_bottom = pygame.image.load(r'D:\Documentos\Área de Trabalho\ratatata\Movimentacao\bottom_1.png')

wall = pygame.Surface((50,50))
ratu = pygame.Surface((50,50))
route = pygame.Surface((50,50))
exit = pygame.Surface((50,50))

route.fill((255,255,255))
exit.fill((255,255,51))
ratu.fill((64,64,64))
wall.fill((51,0,51))

teste = [[1,'m',1,1,1],
         [1,0,0,0,1],
         [1,1,1,0,1],
         [1,0,0,0,1],
         [1,0,1,0,1],
         [1,1,1,'e',1]]


def return_matrix (matrix):
    
    for x in matrix:
        for y  in  x:
            if y == 1:
                screen.blit(wall,(0,0))

quadrados = 0
triangulo = 0

while True:
    
    z = randint(0,1)
    
    if z == 1:
        teste = [[1,'m',1,1,1],
         [1,0,0,0,1],
         [1,1,1,0,1],
         [1,0,0,0,1],
         [1,0,1,0,1],
         [1,1,1,'e',1]]
    else:
        teste = [[1,0,1,1,1],
         [1,0,0,0,1],
         [1,1,1,'m',1],
         [1,0,0,0,1],
         [1,0,1,0,1],
         [1,1,1,'e',1]]
    
    
    for x in teste:
        for y in x:
            if y == 1:
                screen.blit(wall,(quadrados,triangulo))
                quadrados+=  50
            elif y == 'm':
                screen.blit(ratu_bottom,(quadrados,triangulo))
                quadrados+=  50
            elif y == 0:
                screen.blit(route,(quadrados,triangulo))
                quadrados+=  50
            elif y == 'e':
                screen.blit(exit,(quadrados,triangulo))
                quadrados+=  50
                
        triangulo+=50
        quadrados=0
      
    
    triangulo=0
    quadrados=0
    pygame.display.update()
    clock.tick(5)
    
    