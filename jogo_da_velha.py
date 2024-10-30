# Example file showing a basic pygame "game loop"
import pygame #importa a bliblioteca pygame para o script 

# pygame setup # pygame configuração 
pygame.init() # inicialização do pygame
pygame.font.init()#iniciaçizção do pacote do pygames 


screen = pygame.display.set_mode((600,600)) # definição do tamanho da tela 
pygame.display.set_caption('jogo da velha') # nome da janela do jogo 
clock = pygame.time.Clock()


running = True

fonte_quadrinhos=pygame.font.SysFont('Comic Sans Ms ',100,)
runnirg = True #variavel de controle do status do jogo 

x = 0
y = 0


personagem_x = fonte_quadrinhos.render('x',True,'blue')
personagem_y = fonte_quadrinhos.render('o',True,'blue')

jogador_atual = personagem_x # inicializando o jogo com x 

rodadas = 0

tabuleiro_desenhado = False

cordenada_x = 0

cordenada_y = 0

def desenha_tabuleiro(espessura,cor):
     
     
     # desenha tabuleiro 
     #                                  origem    destino
     #                                  (x , y )  (x , y)
    
    pygame.draw.line(screen,cor,(200,0),(200,600),espessura)
    pygame.draw.line(screen,cor,(400,0),(400,600),espessura)
    pygame.draw.line(screen,cor,(0,200),(600,200),espessura)
    pygame.draw.line(screen,cor,(0,400),(600,400),espessura)
    
    print('desenhar')


def faz_jogada():
    print('faz_jogada')
 # determinando o clique das formas (x e o )
    #                             X  Y 
    if cordenada_x > 0 and cordenada_x < 200 and cordenada_y < 200:
        screen.blit(jogador_atual,(60,30)) # primiero 
    
    elif cordenada_x >= 200 and cordenada_x < 400 and cordenada_y < 200: # segundo
        screen.blit(jogador_atual,(260,30))
    
    elif cordenada_x >= 400 and cordenada_y < 200: # terceiro 
        screen.blit(jogador_atual,(460,30))
    
    elif cordenada_x < 200 and cordenada_y >= 200 and cordenada_y<400: # quarto 
        screen.blit(jogador_atual,(60,210))
    
    elif cordenada_x >= 200 and cordenada_x <400 and cordenada_y >= 200 and cordenada_y < 400: # quinto
        screen.blit(jogador_atual,(280,210))
    
    elif cordenada_x >= 400 and cordenada_y >= 200 and cordenada_y < 400: # sexto 
        screen.blit(jogador_atual,(470,210))
    
    elif cordenada_x < 200 and cordenada_y >= 400: # setimo 
        screen.blit(jogador_atual,(60,400))
    
    elif cordenada_x >= 200 and cordenada_x < 400 and cordenada_y >= 400: # oitavo 
        screen.blit(jogador_atual,(280,380))
    
    elif cordenada_x >= 400 and cordenada_y >= 400: # nono 
        screen.blit(jogador_atual,(460,380))
  
 
  
cor_fundo=1 #blue
#cor_fundo=2 #red

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for  event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            print('clicou')
            click_pos = pygame.mouse.get_pos() # a posição do mouse quando houve o evento click
            
            print('eixo x:',click_pos[0])
            cordenada_x = click_pos[0]
            cordenada_y = click_pos[1]
            
            
            print('eixo y:',click_pos[1])
            rodadas = rodadas+1
            
            if(rodadas >= 10):

                screen.fill('black')
                rodadas = 0
                cordenada_x = 0
                cordenada_y = 0
                jogador_atual = personagem_x
                tabuleiro_desenhado = False           
                

            if rodadas != 1:

                if jogador_atual == personagem_x:
                    jogador_atual = personagem_y
                else:
                    jogador_atual=personagem_x
            else:
                jogador_atual = personagem_x

            faz_jogada() 

    if tabuleiro_desenhado == False :
        desenha_tabuleiro(20,'Orange')
        tabuleiro_desenhado = True

personagem_x = fonte_quadrinhos.render('game',True,'red')
personagem_y = fonte_quadrinhos.render('over',True,'red')

fonte_quadrinhos=pygame.font.SysFont('Comic Sans Ms ',100,)
sreen.blit('game',(100,50))
screen.blit('over',(150,100))
   


pygame.display.flip()
     
clock.tick(60)  # limits FPS to 60

pygame.quit ()

