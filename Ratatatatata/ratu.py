import time
import pygame
from labirinto import gerar_mapa as gerar_mapa20
from labirinto import gerar_mapa_geral
import os

def ratu_backend(pegar_text, testa_saida, matrix):
    
    if matrix == None:
        matrix = []
        lista = []

        if pegar_text == True:
            with open ('LABIRINTO.txt') as f:

                for line in f.readlines():
                    for x in line:
                        if x != '\n' and x != 'm' and x != 'e':
                            lista.append(x)
                        elif x == 'm' or  x == 'e':
                            lista.append(x)

                    matrix.append(lista)
                    lista=[]
        else:

            matrix = gerar_mapa_geral()

    def pegar_posicao_rato (matrix):

        linha = 0
        coluna = 0
        lista = []
        for values in matrix:

            for value in values:

                if value  ==  'm':
                    posicao_rato = str(linha) +' '+ str(coluna)
                    print( 'O rato foi encontrado na posicao '+ posicao_rato)
                    lista.append(linha)
                    lista.append(coluna)
                    return lista
                else:
                    coluna += 1
            coluna = 0
            linha += 1

    def pegar_posicao_saida (matrix):

        linha = 0
        coluna = 0
        lista = []
        for values in matrix:

            for value in values:

                if value  ==  'e':
                    posicao_rato = str(linha) +' '+ str(coluna)
                    print( 'O rato foi encontrado na posicao '+ posicao_rato)

                    lista.append(linha)
                    lista.append(coluna)
                    return lista
                else:
                    coluna += 1

            linha += 1
            coluna = 0


    def ratu_movimentar_direita(matrix,posicao_ratu):
        print(posicao_ratu, '<<<<')
        lina_ratu = posicao_ratu[0]
        coluna_ratu = posicao_ratu[1]

        lina_ratu = int(lina_ratu)
        print(posicao_ratu,coluna_ratu, '<<')
        coluna_ratu = int(coluna_ratu)

        try:
            if matrix[lina_ratu][coluna_ratu+1] == '1':
                return False
            if matrix[lina_ratu][coluna_ratu+1] == 'x':
                return False
            else:
                matrix[lina_ratu][coluna_ratu] = 'x'
                matrix[lina_ratu][coluna_ratu+1] = 'm'
                print('->')
                return matrix
        except:
                return False

    def ratu_movimentar_esquerda(matrix,posicao_ratu):
        lina_ratu = posicao_ratu[0]
        coluna_ratu = posicao_ratu[1]

        lina_ratu = int(lina_ratu)
        coluna_ratu = int(coluna_ratu)

        try:
            if matrix[lina_ratu][coluna_ratu-1] == '1':
                return False
            elif matrix[lina_ratu][coluna_ratu-1] == "x":
                return False
            else:
                matrix[lina_ratu][coluna_ratu] = 'x'
                matrix[lina_ratu][coluna_ratu-1] = 'm'
                print('<-')
                return matrix
        except:
            return False

    def ratu_movimentar_baixo(matrix,posicao_ratu):
        lina_ratu = posicao_ratu[0]
        coluna_ratu = posicao_ratu[1]

        lina_ratu = int(lina_ratu)
        coluna_ratu = int(coluna_ratu)

        try:
            if matrix[lina_ratu+1][coluna_ratu] == '1':
                return False
            elif matrix[lina_ratu+1][coluna_ratu] == "x":
                return False
            else:
                matrix[lina_ratu][coluna_ratu] = 'x'
                matrix[lina_ratu+1][coluna_ratu] = 'm'
                print('v')
                return matrix
        except:
            return False

    def ratu_movimentar_cima(matrix,posicao_ratu):
        lina_ratu = posicao_ratu[0]
        coluna_ratu = posicao_ratu[1]

        lina_ratu = int(lina_ratu)
        coluna_ratu = int(coluna_ratu)

        try:
            if matrix[lina_ratu-1][coluna_ratu] == '1':
                return False
            elif matrix[lina_ratu-1][coluna_ratu] == "x":
                return False
            else:
                matrix[lina_ratu][coluna_ratu] = 'x'
                matrix[lina_ratu-1][coluna_ratu] = 'm'
                print('T')
                return matrix
        except:
            return False
        

    #print(matrix)
    pegar_posicao_rato(matrix)

    posicao_rato  = pegar_posicao_rato(matrix)
    posicao_saida  = pegar_posicao_saida(matrix)
    #print(posicao_rato, posicao_saida,  ',,,')

    pilha_jornada = []
    pilha_ratu = []

    pilha_ratu.append(posicao_rato)
    pilha_jornada.append(posicao_rato)


    catch =  pilha_ratu[-1]

    pygame.init()
    screen = pygame.display.set_mode((1220,700))
    screen.fill('white')
    
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 60)
    
    clock = pygame.time.Clock()

    
    wall = pygame.Surface((61,36))
    ratu = pygame.Surface((61,36))
    route = pygame.Surface((61,36))
    exit = pygame.Surface((61,36))
    zed = pygame.Surface((61,36))
    
    route.fill((255,255,255))
    exit.fill((255,255,51))
    ratu.fill((64,64,64))
    wall.fill((51,0,51))
    zed.fill((255,153,204))
    
    ratu_direçao = 0
    rato_img = 0
    
    ratu_top_1 = pygame.image.load('Movimentacao/top_1.png')
    ratu_top_2 = pygame.image.load('Movimentacao/top_2.png')
    
    ratu_right_1 = pygame.image.load('Movimentacao/right_1.png')
    ratu_right_2 = pygame.image.load('Movimentacao/right_2.png')
    
    ratu_bottom_1 = pygame.image.load('Movimentacao/bottom_1.png')
    ratu_bottom_2 = pygame.image.load('Movimentacao/bottom_2.png')
    
    ratu_left_1 = pygame.image.load('Movimentacao/left_1.png')
    ratu_left_2 = pygame.image.load('Movimentacao/left_2.png')
    
    barreira = pygame.image.load('Movimentacao/barreira.png')
    queijo = pygame.image.load('Movimentacao/queijo.png')
    
    sucesso = pygame.image.load('Movimentacao/sucesso.png')
    
    ground_ = pygame.image.load('Movimentacao/ground_walked1.png')
    ground = pygame.image.load('Movimentacao/ground_teste.png')
    
    
    ground_ = pygame.transform.scale(ground_, ((62,36)))
    ground = pygame.transform.scale(ground, ((62,36)))
    barreira = pygame.transform.scale(barreira, ((60,36)))
    queijo = pygame.transform.scale(queijo, ((50,36)))
    
    quadrados = 0
    triangulo = 0

    if testa_saida == 1:
        try:
            while pilha_ratu[-1] != posicao_saida:

                #print(pilha_ratu, '<<<< posição do ratu')
                rm_pilha = 0

                x = 0
                x = ratu_movimentar_direita(matrix, pilha_ratu[-1])
                if x == False:
                    x=  ratu_movimentar_esquerda(matrix, pilha_ratu[-1])
                    if x == False:
                        x=  ratu_movimentar_baixo(matrix, pilha_ratu[-1])
                        if x == False:
                            x=  ratu_movimentar_cima(matrix, pilha_ratu[-1])
                            if x == False:
                                rm_pilha =  1
                                y = pilha_ratu[-1]
                                lina_ratu = y[0]
                                coluna_ratu = y[1]
                                lina_ratu = int(lina_ratu)
                                coluna_ratu = int(coluna_ratu)
                                matrix [lina_ratu][coluna_ratu] = 'x'
                                pilha_jornada.append(pilha_ratu[-1])
                                pilha_ratu.pop()

                            else:
                                matrix = x               
                        else:
                            matrix = x            
                    else:
                        matrix = x
                else:
                    matrix = x
                if posicao_rato == posicao_saida:
                    break
                if rm_pilha ==  0:
                    #time.sleep(0.5) #diminuir a velocidade do ratu
                    posicao_rato  = pegar_posicao_rato(matrix)
                    pilha_ratu.append(posicao_rato)
                    pilha_jornada.append(posicao_rato)

            #print('O rato achou a saida')
            #print('Pilha:', pilha_ratu)
            #input()
            return ratu_backend(pegar_text, 0, None)

        except IndexError:
            #print('O rato ficou preso e não achou a saida GG ;-;\nJornada do  rato', pilha_jornada, '<<<' )

            #print('>'*25,'Aperte qualquer coisa para tentar dnv.','<'*25)
            #input()
            ratu_backend(pegar_text, 1, None)
    else:

        
        try:
            
            
            while pilha_ratu[-1] != posicao_saida:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                
                
                print(pilha_ratu, '<<<< posição do ratu')
                rm_pilha = 0

                x = 0
                x = ratu_movimentar_direita(matrix, pilha_ratu[-1])
                if x == False:
                    x=  ratu_movimentar_esquerda(matrix, pilha_ratu[-1])
                    if x == False:
                        x=  ratu_movimentar_baixo(matrix, pilha_ratu[-1])
                        if x == False:
                            x=  ratu_movimentar_cima(matrix, pilha_ratu[-1])
                            if x == False:
                                rm_pilha =  1
                                y = pilha_ratu[-1]
                                lina_ratu = y[0]
                                coluna_ratu = y[1]
                                lina_ratu = int(lina_ratu)
                                coluna_ratu = int(coluna_ratu)
                                matrix [lina_ratu][coluna_ratu] = 'x'
                                pilha_jornada.append(pilha_ratu[-1])
                                pilha_ratu.pop()

                            else:
                                ratu_direçao = 'cima'
                                rato_img += 1
                                matrix = x               
                        else:
                            ratu_direçao = 'baixo'
                            rato_img += 1
                            matrix = x            
                    else:
                        ratu_direçao = 'esquerda'
                        rato_img += 1
                        matrix = x
                else:
                    
                    ratu_direçao = 'direita'
                    rato_img += 1
                    matrix = x
                    
                if posicao_rato == posicao_saida:
                    break
                if rm_pilha ==  0:
                    time.sleep(0) #diminuir a velocidade do ratu
                    for valores in matrix:
                        print(''.join(str(valores)).replace("'", ""))
                    posicao_rato  = pegar_posicao_rato(matrix)
                    pilha_ratu.append(posicao_rato)
                    pilha_jornada.append(posicao_rato)
                    
                    for x in matrix:
                        for y in x:
                            if y == '1':
                                screen.blit(ground,(quadrados,triangulo-4))
                                screen.blit(barreira,(quadrados,triangulo))
                                quadrados+=  61
                            elif y == 'm':
                                
                                if ratu_direçao == 'direita' and rato_img % 2 == 0:
                                    screen.blit(ratu_right_1,(quadrados+5,triangulo-4))
                                elif ratu_direçao == 'direita'  and rato_img % 2 != 0:
                                    screen.blit(ratu_right_2,(quadrados+5,triangulo-4))
                                    
                                elif  ratu_direçao == 'esquerda' and rato_img % 2 == 0:
                                    screen.blit(ratu_left_1,(quadrados+5,triangulo-4))
                                elif ratu_direçao == 'esquerda' and rato_img % 2 != 0:
                                    screen.blit(ratu_left_2,(quadrados+5,triangulo-4))  
                                    
                                elif  ratu_direçao == 'baixo' and rato_img % 2 == 0:
                                    screen.blit(ratu_bottom_1,(quadrados+5,triangulo-4))
                                elif ratu_direçao == 'baixo' and rato_img % 2 != 0:
                                    screen.blit(ratu_bottom_1,(quadrados+5,triangulo-4))  
                                    
                                elif  ratu_direçao == 'cima' and rato_img % 2 == 0:
                                    screen.blit(ratu_top_1,(quadrados+5,triangulo-4))
                                elif ratu_direçao == 'cima' and rato_img % 2 != 0:
                                    screen.blit(ratu_top_1,(quadrados+5,triangulo-4))  
                                    
                                quadrados+=  61
                                
                            elif y == '0':
                                
                                screen.blit(ground,(quadrados,triangulo-4))
                                quadrados+=  61
                            elif y == 'e':
                                screen.blit(ground,(quadrados,triangulo-4))
                                screen.blit(queijo,(quadrados,triangulo-4))
                                quadrados+=  61
                            elif y == 'x':
                                screen.blit(ground_,(quadrados,triangulo-4))
                                quadrados+=  61

                        triangulo+=36
                        quadrados=0

                    time.sleep(0.1)  
                    triangulo=0
                    quadrados=0
                    
                    if pilha_ratu[-1] == posicao_saida:
                        string_pilha = str()
                        
                        for x in pilha_ratu:
                            string_pilha += str(x)
                            
                        text_surface = my_font.render('Sucesso', False, (67, 2, 110))
                 
                        screen.blit(text_surface, (500,275))
                        screen.blit(sucesso,(720,200))
                    
                    pygame.display.update()
                    clock.tick(60)
                    
                    
                    
                else: 
                    for valores in matrix:
                        print(''.join(str(valores)).replace("'", ""))
            print('O rato achou a saida')
            print('Pilha:', pilha_ratu)
            input('>>>>> gg <<<<<')
            

        except IndexError:
            print('O rato ficou preso e não achou a saida GG ;-;\nJornada do  rato', pilha_jornada, '<<<' )

            print('>'*25,'Aperte qualquer coisa para tentar dnv.','<'*25)
            ratu_backend(True, 1, None)
        print('tem saiu')
        
ratu_backend(False, 1, None)