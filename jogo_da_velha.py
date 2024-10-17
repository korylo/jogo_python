import pygame  # importa a biblioteca

# pygame setup
pygame.init()  # inicialização do pygame
pygame.font.init()  # inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((500, 500)) #Essa função configura a janela onde o jogo será exibido.
pygame.display.set_caption('jogo da Velha ') #Esta função altera o título da janela que é exibida na barra de título do aplicativo.
clock = pygame.time.Clock() # Esse objeto é usado para gerenciar o tempo no seu jogo, permitindo que você controle a velocidade de atualização da tela.




fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100)  #função é usada para criar uma fonte a partir de fontes disponíveis no sistema operacional. 
#Ela permite que você escolha uma fonte já instalada em seu sistema.

running = True  #A variável `running` é usada como uma condição para determinar se o loop principal do jogo deve continuar girando ou não.
#Quando `running` é `True`, o loop continua; quando `running` se torna `False`

# cria uma superfície de imagem a partir do texto que você deseja exibir na tela."X" e "0"
personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('0', True, 'red')
cor_fundo = 1 # a inicializa com o valor `1`. Essa variável é geralmente usada para controlar o fundo da tela em um jogo, 
#permitindo a alternância entre diferentes núcleos

while running: # O whileé usado para repetir um bloco de código enquanto uma condição é verdadeira.  

    for event in pygame.event.get():# Esta função retorna uma lista de todos os eventos que ocorreram desde a última vez que você chamou essa função. 
        #Isso inclui eventos como cliques de mouse, teclas pressionadas, movimentos de mouse e comandos de fechamento de janela.

        if event.type == pygame.QUIT: #Detectar quando o usuário tenta fechar uma janela do jogo.
            #Permite que você responda a esse evento encerrando o loop principal e fechando o jogo de forma adequada.

            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # pressionar uma tecla, mover o mouse, ou um clique do mouse)
            print('Clicou')#é um comando que exibe a mensagem "Clicou" no console ou na saída padrão do programa.
            cor_fundo += 1
        if cor_fundo > 3: # é uma condição que verifica se o valor da variável `cor_fundo` é maior que 3. 
            cor_fundo = 1

    
    if cor_fundo == 1:#uma estrutura condicional que executa um bloco de código se a condição especificada for verdadeira. 
        #Neste caso, ele verifica se `cor_fundo` é igual a `1`. 2.

        screen.fill('blue')  #  preenche toda a superfície da tela com uma cor específica. azul

        screen.blit(personagem_x, (250, 250))  # para desenhar uma superfície (como uma imagem ou texto) na tela. Desenha "X" 

    elif cor_fundo == 2:# Verifique se `cor_fundo` é igual a ` 2` para determinar a ação a ser tomada. 

        screen.fill('blue')  # Preenche com azul
        screen.blit(personagem_y, (250, 250))  # # para desenhar uma superfície (como uma imagem ou texto) na tela. Desenha "0"
    else:
        screen.fill('purple')  ##  preenche toda a superfície da tela com uma cor específica.rosa

    # ara atualizar a tela do jogo com todas as alterações que foram feitas desde a última atualização.
    pygame.display.flip()

    clock.tick(60)  #  é um objeto utilizado para controlar o tempo e a taxa atualização do jogo.

pygame.quit() # encerrar a biblioteca e limpar todos os recursos que foram utilizados durante a execução do jogo. 
