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


personagem_x=fonte_quadrinhos.render('x',True,'blue')
personagem_y=fonte_quadrinhos.render('o',True,'blue')
apresenta_personagem=0
x=0
y=0

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
            click_pos= pygame.mouse.get_pos() # a posição do mouse quando houve o evento click
            print('eixo x:',click_pos[0])
            x=click_pos[0]
            y= click_pos[1]
            print('eixo y:',click_pos[1])
            apresenta_personagem=apresenta_personagem+1
            if(apresenta_personagem>=10):
                screen.fill('black')
                apresenta_personagem=0

     # desenha tabuleiro 
     #                                  origem    destino
     #                                  (x , y )  (x , y)
    
    pygame.draw.line(screen,'white',(200,0),(200,600),10)
    pygame.draw.line(screen,'white',(400,0),(400,600),10)
    pygame.draw.line(screen,'white',(0,200),(600,200),10)
    pygame.draw.line(screen,'white',(0,400),(600,400),10)
   


    # determinando o clique das formas (x e o )
    #                             X  Y 
    if x>0 and x<200 and y<200:
        screen.blit(personagem_x,(60,30)) # primiero 
    
    elif x>=200 and x<400 and y<200: # segundo
        screen.blit(personagem_y,(260,30))
    
    
    elif x>=400 and y<200: # terceiro 
        screen.blit(personagem_x,(460,30))
    
    elif x<200 and y >=200 and y<400: # quarto
        screen.blit(personagem_y,(60,210))
    
    elif x>=200 and x<400 and y >=200 and y<400: # quinto
        screen.blit(personagem_x,(280,210))
    
    
    elif x>=400 and y>=200 and y<400: # sexto 
        screen.blit(personagem_y,(470,210))
    
    elif x<200 and y>=400: # setimo 
        screen.blit(personagem_x,(60,400))
    
    elif x>=200 and x<400 and y>=400: # oitavo 
        screen.blit(personagem_y,(280,380))
    
    elif x>=400 and y>=400: # nono 
        screen.blit(personagem_x,(460,380))
  
    pygame.display.flip()
     
    clock.tick(60)  # limits FPS to 60

pygame.quit ()


