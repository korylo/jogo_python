import pygame  # importa a biblioteca

# pygame setup
pygame.init()  # inicialização do pygame
pygame.font.init()  # inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #Essa função configura a janela onde o jogo será exibido.
pygame.display.set_caption('jogo da Velha ') #Esta função altera o título da janela que é exibida na barra de título do aplicativo.
clock = pygame.time.Clock() # Esse objeto é usado para gerenciar o tempo no seu jogo, permitindo que você controle a velocidade de atualização da tela.




fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100)  #função é usada para criar uma fonte a partir de fontes disponíveis no sistema operacional. 
#Ela permite que você escolha uma fonte já instalada em seu sistema.

running = True  #A variável `running` é usada como uma condição para determinar se o loop principal do jogo deve continuar girando ou não.
#Quando `running` é `True`, o loop continua; quando `running` se torna `False`

# cria uma superfície de imagem a partir do texto que você deseja exibir na tela."X" e "0"
personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_o = fonte_quadrinhos.render('0', True, 'red')

jogador_atual = personagem_x #inicializa o jogo com o x.

rodadas = 0 
tabuleiro_desenhado = False
coordenada_x = 0
coordenada_y = 0

q1 = ''
q2 = ''
q3 = ''
q4 = ''
q5 = ''
q6 = ''
q7 = ''
q8 = ''
q9 = ''

def desenha_tabuleiro(espessura,cor):





    
    
    
     # desenha tabuleiro             (x)  (y)  (x)  (y)
    pygame.draw.line(screen, 'yellow',(200, 0),(200, 600),espessura)
    pygame.draw.line(screen, 'yellow',(400, 0),(400, 600),espessura)
    pygame.draw.line(screen, 'yellow',(0, 200),(600, 200),espessura)
    pygame.draw.line(screen, 'yellow',(0, 400),(600, 400),espessura)

def faz_jogada():
    global q1, q2, q3, q4, q5, q6, q7, q8, q9
    status = True
      
    if q1 ==''and coordenada_x > 0 and coordenada_x < 200 and coordenada_y < 200:  # (x),(y)
       screen.blit(jogador_atual,(60,30)) #primario
       q1 = jogador_atual
    elif q2 ==''and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y < 200:   
        screen.blit(jogador_atual,(260,30)) #segundario
        q2 = jogador_atual
    elif q3 ==''and coordenada_x >= 400 and coordenada_y < 200:   
        screen.blit(jogador_atual,(460,30)) #terceiro
        q3 = jogador_atual

    #segundario linha
    #
    elif q4 ==''and coordenada_x < 200 and coordenada_y >= 200 and coordenada_y <400:
        screen.blit(jogador_atual,(60,230)) #quarto
        q4 = jogador_atual
    elif q5 ==''and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 200 and coordenada_y < 400:   
        screen.blit(jogador_atual,(260,230)) #quinto
        q5 = jogador_atual
    elif q6 ==''and coordenada_x >= 400 and coordenada_y >= 200 and coordenada_y < 400:     
        screen.blit(jogador_atual,(460,230)) #sexto
        q6 = jogador_atual

     #terceiro linha
    #
    elif q7 ==''and coordenada_x < 200 and coordenada_y >= 400:
        screen.blit(jogador_atual,(60,430)) #setimo
        q7 == jogador_atual
    elif q8 ==''and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 400: 
        screen.blit(jogador_atual,(260,430)) #oitavo
        q8 == jogador_atual
    elif q9 ==''and coordenada_x >= 400 and coordenada_y >= 400:       
        screen.blit(jogador_atual,(460,430)) #nono
        q9 = jogador_atual
    else:
        status = False 
    return status 
def check_vencedor(): 
    #linhas
    status = False
    if q1 == q2 == q3 != "":
        pygame.draw.line(screen, 'orange',(50, 100),(550, 100),10)
        status =True
        
    elif q4 == q5 == q6 != "":
        pygame.draw.line(screen, 'yellow',(50, 300),(550, 300),10)
        status =True
        
    elif q7 == q8 == q9 != "":
        pygame.draw.line(screen, 'yellow',(50, 500),(550, 500),10)
        status =True
        

    #colunas
    elif q1 == q4 == q7 != "":
        pygame.draw.line(screen, 'yellow',(100, 500),(300, 500),10)
        status =True
        
    elif q2 == q5 == q8 != "":
        pygame.draw.line(screen, 'yellow',(100, 200),(300, 200),10)
        status =True
        
    elif q3 == q6 == q9 != "":
        pygame.draw.line(screen, 'yellow',(100, 500),(300, 500),10)
        status =True
          

    #diagonais 
    elif q1 == q5 == q9 != "":
        status =True
        
    elif q3 == q5 == q7 != "":
        status =True
    return status
        
                             

while running: # codigo principal. 

    for event in pygame.event.get():# Esta função retorna uma lista de todos os eventos que ocorreram desde a última vez que você chamou essa função. 
        #Isso inclui eventos como cliques de mouse, teclas pressionadas, movimentos de mouse e comandos de fechamento de janela.
    

        if event.type == pygame.QUIT: #Detectar quando o usuário tenta fechar uma janela do jogo.
            #Permite que você responda a esse evento encerrando o loop principal e fechando o jogo de forma adequada.
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # pressionar uma tecla, mover o mouse, ou um clique do mouse)
            print('Clicou')#é um comando que exibe a mensagem "Clicou" no console ou na saída padrão do programa.
            click_pos =pygame.mouse.get_pos()#a posiçao do mouse quando ouver evento de click
            print("eixo x:",click_pos[0])
            print("eixo y:",click_pos[1])
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]

            if(rodadas >= 9) : 
                screen.fill('black')
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                jogador_atual =personagem_x
                tabuleiro_desenhado =False
                break
            if(faz_jogada()):
                rodadas = rodadas + 1   
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o         
                else:
                   jogador_atual =personagem_x 
                if(check_vencedor()):
                    rodadas = 9  
               
           

            
            
           
        
    
    if tabuleiro_desenhado == False:   
        desenha_tabuleiro(10,'yellow')
        q1 = ''
        q2 = ''
        q3 = ''
        q4 = ''
        q5 = ''
        q6 = ''
        q7 = ''
        q8 = ''
        q9 = ''
        tabuleiro_desenhado = True

    
     
    #primario linha
     #  
    
      

    # ara atualizar a tela do jogo com todas as alterações que foram feitas desde a última atualização.
    pygame.display.flip()

    clock.tick(60)  #  é um objeto utilizado para controlar o tempo e a taxa atualização do jogo.

pygame.quit() # encerrar a biblioteca e limpar todos os recursos que foram utilizados durante a execução do jogo. 
