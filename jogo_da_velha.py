# Example file showing a basic pygame "game loop"
import pygame

# pygame configuração
pygame.init()#inicialização do pygame
pygame.font.init() #inicialização do pacote de fonte no pygame
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("jogo da velha")
clock = pygame.time.Clock()#biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms',100) #importando fontes
running = True
personagem_X = fonte_quadrinhos.render('X',True, 'red')
personagem_Y = fonte_quadrinhos.render('O',True, 'red')
cor_fundo = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('clicou')
            cor_fundo = cor_fundo + 1
            if(cor_fundo >3):
              cor_fundo = 1
        
        
    if cor_fundo == 1:
        screen.fill('black')
        screen.blit (personagem_X,(250,250))
    elif cor_fundo == 2:
        screen.fill('black')
        screen.blit (personagem_Y,(250,250))
    else:
        screen.fill('purple')  
              

    # flip() the display para atualiza a pagina 
    pygame.display.flip()

    clock.tick(60)  # limits FPS para  60

pygame.quit()