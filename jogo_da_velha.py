# Example file showing a basic pygame "game loop"
import pygame #importa a bliblioteca pygame para o script 

# pygame setup # pygame configuração 
pygame.init() # inicialização do pygame
pygame.font.init()#iniciaçizção do pacote do pygames 


screen = pygame.display.set_mode((600,600)) # definição do tamanho da tela 
pygame.display.set_caption('jogo da velha') # nome da janela do jogo 
clock = pygame.time.Clock()


running = True

fonte_quadrinhos=pygame.font.SysFont('Comic Sans Ms ',100,True,True )
runnirg=True #variavel de controle do status do jogo 

personagem_x=fonte_quadrinhos.render('x',True,'red')
personagem_y=fonte_quadrinhos.render('o',True,'red')
cor_fundo=1

cor_fundo=1 #blue
#cor_fundo=2 #red
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            print('clicou')
            cor_fundo=cor_fundo+1
            if(cor_fundo>3):
                cor_fundo=1

     # desenha tabuleiro 
     #                                  origem    destino
     #                                  (x , y )  (x , y)
        pygame.draw.line(screen,'white',(200,0),(200,600),10)
        pygame.draw.line(screen,'white',(400,0),(400,600),10)
        pygame.draw.line(screen,'white',(0,200),(600,200),10)
        pygame.draw.line(screen,'white',(0,400),(600,400),10)
   
    #                             x   y 
        screen.blit(personagem_x,(60,30))#primeiro 
        screen.blit(personagem_y,(260,30))#segundo 
        screen.blit(personagem_y,(460,30))#terceiro
         
  
    pygame.display.flip()
     
    clock.tick(60)  # limits FPS to 60

pygame.quit ()


