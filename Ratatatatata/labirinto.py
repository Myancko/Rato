from random import randint
import time
import numpy

import os

def gerar_mapa_geral(LINHAS = 20, COLUNAS = 20):
    """Gera o mapa aleatorio q sera usado pelo rato"""
    
    matrix = numpy.zeros(shape=(LINHAS, COLUNAS)).astype(int)

    count = 0
    while count < COLUNAS:
        #cima
        matrix[0][count] = 1
        count +=1

    count = 0
    while count < LINHAS:
        #direita
        matrix[count][COLUNAS-1] = 1
        count +=1
        
    count = 0
    while count < COLUNAS:
        #baixo
        matrix[LINHAS-1][count] = 1
        count +=1
    count = 0
    while count < LINHAS:
        #esquerda
        matrix[count][0] = 1
        count +=1
    
    
    """ pegar extremidades da matrix"""
    count = 0
    for x in matrix:
        for y in x:
            if y == 1:
                count += 1
                
    #print(count, '<<<')
    
    if count % 2 == 0:
        pass
    else:
        print('matrix impar')
        #input()
        gerar_mapa_geral(LINHAS+1,COLUNAS)
        
    #print(matrix)
    
    """Gerar saida"""
    
    direcao = randint(0,3)
    
        
    if direcao == 0:
        #cima
        saida = randint(0, COLUNAS-1)
        if saida == 0:
            matrix [0][saida] = 54
            matrix [0][saida+1] = 0
            matrix [1][saida] = 0
        elif saida == COLUNAS-1:
            matrix [0][saida] = 54
            matrix [0][saida-1] = 0
            matrix [1][saida] = 0
        else:
            matrix [0][saida] = 54

    elif direcao == 1:
        #direta
        saida = randint(0, LINHAS-1)
        if saida == 0:
            matrix [saida][LINHAS-1] = 54
            matrix [saida][LINHAS-2] = 0
            matrix [saida+1][LINHAS-1] = 0

        elif saida == LINHAS-1:
            matrix [saida][LINHAS-1] = 54
            matrix [saida][LINHAS-2] = 0
            matrix [saida-1][LINHAS-1] = 0

        else:
            matrix [saida][COLUNAS-1] = 54
    
    elif direcao == 2:
        #baixo
        saida = randint(0, COLUNAS-1)
        if saida == 0:
            matrix [LINHAS-1][saida] = 54
            matrix [LINHAS-2][saida] = 0
            matrix [LINHAS-1][saida+1] = 0
        elif saida == COLUNAS-1:
            matrix [LINHAS-1][saida] = 54
            matrix [LINHAS-2][saida] = 0
            matrix [LINHAS-1][saida-1] = 0
        else:
            matrix [LINHAS-1][saida] = 54

    elif direcao == 3:
        #esquerda
        
        saida = randint(0, LINHAS-1)
        if saida == 0:
            matrix [saida][0] = 54
            matrix [saida][0+1]= 0
            matrix [saida+1][0] = 0
        elif saida == LINHAS-1:
            matrix [saida][0] = 54
            matrix [saida][0+1] = 0
            matrix [saida-1][0] = 0
        else:
            matrix [saida][0] = 54
            
            
    """ gera o rato """
    direcao_rato = randint(0,3)
    while direcao_rato == direcao:
            
        direcao_rato = randint(0,3)
    
    if direcao_rato == 0:
            rato = randint(1,COLUNAS-2)
            matrix [0][rato] = 69   
    if direcao_rato == 1:
            rato = randint(1,LINHAS-2)
            matrix [rato][COLUNAS-1] = 69 
    if direcao_rato == 2:
            rato = randint(1,COLUNAS-2)
            matrix [LINHAS-1][rato] = 69 
    if direcao_rato == 3:
            rato = randint(1,LINHAS-2)
            matrix [rato][0] = 69 
            
            
            
    """Gerar Barreiras"""
    x = 0
    if LINHAS > COLUNAS:
        x = LINHAS
    else:
        x = COLUNAS

    NUMERO_DE_BARREIRAS = int(x / 1.2)
    count_barreira = 0
    #print(NUMERO_DE_BARREIRAS, 'total esperado de barreiras')
    holder = 0


    while count_barreira < NUMERO_DE_BARREIRAS:

        b_linhas = randint(2,LINHAS-2)
        b_colunas = randint(2,COLUNAS-2)
        
        direcao = randint(0, 3)
        
        if direcao == 0:
            #direita

            while b_colunas != COLUNAS-2:
                dot = randint(0, 5)
                
                if dot > 2:
                    matrix[b_linhas][b_colunas] = 1
                    b_colunas+=1
                    
                else:
                    b_colunas+=1
                    
        elif direcao == 1:
            #baixo
            
            while b_linhas != LINHAS-2:
                dot = randint(0, 5)
                
                if dot > 2:
                    matrix[b_linhas][b_colunas] = 1
                    b_linhas+=1
                    
                else:
                    b_linhas+=1
        
        elif direcao == 2:
            #esquerda
            
            while b_colunas != COLUNAS-2:
                
                if b_colunas == 2:
                    break
                
                dot = randint(0, 5)
                
                if dot > 2:
                    matrix[b_linhas][b_colunas] = 1
                    b_colunas-=1
                    
                else:
                    b_colunas-=1
                    
        elif direcao == 3:
            #cima
            
            while b_linhas != LINHAS-2:
                dot = randint(0, 5)
                
                if b_linhas == 2:
                    break
                
                if dot > 2:
                    matrix[b_linhas][b_colunas] = 1
                    b_linhas-=1
                    
                else:
                    b_linhas-=1

        count_barreira += 1

    
    nova_matrix = []
    helper = []
    
    
    for x in matrix:
        for y in x:
            #print(y)
            if y == 69:
                helper.append('m')
            elif y == 54:
                helper.append('e')
            else:
                helper.append(str(y))
                
        nova_matrix.append(helper)
        helper = []
        
   
    return nova_matrix

    



def gerar_mapa():
    """Gera o mapa aleatorio de apenas 20 linhas e colunas"""
    LINHAS = 20
    COLUNAS = 20

    matrix = numpy.zeros(shape=(LINHAS, COLUNAS)).astype(int)
    print(matrix)


    #criar tabuleiro fechado
    count = 0
    while count < 20:

        matrix[count][0] = 1
        count +=1

    count = 0
    while count < 20:

        matrix[19][count] = 1
        count +=1
    count = 0
    while count < 20:

        matrix[count][19] = 1
        count +=1
    count = 0
    while count < 20:

        matrix[0][count] = 1
        count +=1
    count = 0

    #criar uma saida aleatoria.
    os.system('cls')

    saida = randint(0,79)
    rato = randint(0,79)
    print(saida, '<<<<<<')
    if saida <= 19:
        #cima
        if saida == 0:
            matrix [0][saida] = 54
            matrix [0][saida+1] = 0
            matrix [1][saida] = 0
        elif saida == 19:
            matrix [0][saida] = 54
            matrix [0][saida-1] = 0
            matrix [1][saida] = 0

        else:
            matrix [0][saida] = 54



    elif saida > 19 and saida < 40:
        #direta

        if saida == 20:
            matrix [saida-COLUNAS][COLUNAS-1] = 54
            matrix [saida-COLUNAS][COLUNAS-2] = 0
            matrix [saida-COLUNAS+1][COLUNAS-1] = 0

        elif saida == 39:
            matrix [saida-COLUNAS][COLUNAS-1] = 54
            matrix [saida-COLUNAS][COLUNAS-2] = 0
            matrix [saida-COLUNAS-1][COLUNAS-1] = 0

        else:
            matrix [saida-COLUNAS][COLUNAS-1] = 54



    elif saida > 39 and saida < 60:
        #baixo
        if saida  == 40:
            matrix [LINHAS-1][saida - (COLUNAS*2)] = 54
            matrix [LINHAS-2][saida - (COLUNAS*2)] = 0
            matrix [LINHAS-1][saida - (COLUNAS*2 -1)] = 0
        elif saida == 59:
            matrix [LINHAS-1][saida - (COLUNAS*2)] = 54
            matrix [LINHAS-2][saida - (COLUNAS*2)] = 0
            matrix [LINHAS-1][saida - (COLUNAS*2 +1)] = 0
        else:
            matrix [LINHAS-1][saida - (COLUNAS*2)] = 54
    elif saida > 59 and saida < 80:
        #esquerda
        if saida == 60:
            matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS] = 54
            matrix [saida-(LINHAS*3-1)][COLUNAS-COLUNAS] = 0
            matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS+1] = 0
        elif saida == 79:
            matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS] = 54
            matrix [saida-(LINHAS*3+1)][COLUNAS-COLUNAS] = 0
            matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS+1] = 0
        else:
            matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS] = 54


    #criar as barreiras

    NUMERO_DE_BARREIRAS = int(COLUNAS / 1.5)
    count_barreira = 0
    print(NUMERO_DE_BARREIRAS, 'total esperado de barreiras')
    holder = 0


    while count_barreira < NUMERO_DE_BARREIRAS:

        b_linhas = randint(2,18)
        b_colunas = randint(2,18)


        direcao  = randint(0, 1)
        if direcao == 0:
            #direita

            while b_colunas != 19:
                dot = randint(0, 1)
                if dot == 1 and b_linhas != 0:
                    matrix[b_linhas][b_colunas] = 1
                    b_colunas +=1
                else:
                    b_colunas +=1

        elif direcao == 1:
            #baixo
            while b_linhas != 19:
                dot = randint(0, 1)
                if dot == 1 and  b_linhas != 0:
                    matrix[b_linhas][b_colunas] = 1
                    b_linhas +=1
                else:
                    b_linhas +=1

        elif direcao == 2:
            #esquerda
            while b_linhas != 19 and b_linhas != 0:
                dot = randint(0, 1)
                if dot == 1:
                    matrix[b_linhas][b_colunas] = 1
                    b_linhas -=1
                else:
                    b_linhas -=1

        elif direcao == 3:
            #cima
            while b_linhas != 19:
                dot = randint(0, 1)
                if dot == 1 and b_linhas != 0:
                    matrix[b_linhas][b_colunas] = 1
                    b_colunas -=1
                else:
                    b_colunas -=1 
        count_barreira += 1


    #gera o rato
    if rato <= 19:
            matrix [0][rato] = 69   
    if rato > 19 and rato < 40:
            matrix [rato-COLUNAS][COLUNAS-1] = 69
    if rato > 39 and rato < 60:
            matrix [LINHAS-1][rato - (COLUNAS*2)] = 69
    if rato > 59 and rato < 80:
            matrix [rato-(LINHAS*3)][COLUNAS-COLUNAS] = 69


    print(matrix)
    print(matrix[0][0])


    nova_matrix = []
    helper = []
    
    
    for x in matrix:
        for y in x:
            print(y)
            if y == 69:
                helper.append('m')
            elif y == 54:
                helper.append('e')
            else:
                helper.append(str(y))
                
        nova_matrix.append(helper)
        helper = []
        
    for x in nova_matrix:
        print(x)
    return nova_matrix

if __name__ == '__main__':
    gerar_mapa_geral()