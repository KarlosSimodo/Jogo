#imports
from random import randint
import pygame
from os import path
#importa casas e jogos
from CASA1 import CASA1
from CASA2 import CASA2
from CASA3 import CASA3
from CASA4 import CASA4
from CASA5 import CASA5
from CASA6 import CASA6
from CASA7 import CASA7
from CASA8 import CASA8
from JoKenPo import JOKENPO
from Forca import FORCA
from MinigameCesta import CESTA
pasta_img=path.join(path.dirname(__file__), 'imagens')

#"fases" do jogo
instrucao = 0
jogo = 1
fim = 2

#variaveis
    #tela
altura=600
largura=1000
    #cores
azul=(0,0,255)
verde=(0,200,0)
preto=(0,0,0)
cinza=(127,127,127)
vermelho=(230,170,0)
branco=(255,255,255)
amarelo=(255,255,0)
roxo=(200,0,200)

    #posicao 
posi_joga=[100,100]
posi_bot_1=[100,100]
posi_bot_2=[100,100]
resultado_jogo_coordenadas=(largura/2,altura/2)

#inicia jogo
pygame.init()
pygame.mixer.init()
window=pygame.display.set_mode((largura,altura))
background = pygame.image.load(path.join(pasta_img,"telainicialpygame.jpg")).convert()
pygame.display.set_caption('JOGO')

#fontes
font= pygame.font.SysFont(None,36)
fontt= pygame.font.SysFont(None,23)
fontdado= pygame.font.SysFont(None,90)

#posicao das casas
vertini=[(75,50),(75,150),(150,150),(150,50)]
vert1=[(151,50),(151,150),(251,150),(251,50)]
vert2=[(252,50),(252,150),(352,150),(352,50)]
vert3=[(353,50),(353,150),(453,150),(453,50)]
vert4=[(454,50),(454,150),(554,150),(554,50)]
vert5=[(555,50),(555,150),(655,150),(655,50)]
vert6=[(656,50),(656,150),(756,150),(756,50)]
vert7=[(757,50),(757,150),(857,150),(857,50)]
vert8=[(757,151),(857,151),(857,251),(757,251)]
vert9=[(757,252),(857,252),(857,352),(757,352)]
vert10=[(656,252),(756,252),(756,352),(656,352)]
vert11=[(555,252),(655,252),(655,352),(555,352)]
vert12=[(454,252),(554,252),(554,352),(454,352)]
vert13=[(353,252),(453,252),(453,352),(353,352)]
vert14=[(252,252),(352,252),(352,352),(252,352)]
vert15=[(151,252),(251,252),(251,352),(151,352)]
vert16=[(151,352),(251,352),(251,453),(151,453)]
vert17=[(151,453),(251,453),(251,554),(151,554)]
vert18=[(252,453),(352,453),(352,554),(252,554)]
vert19=[(353,453),(453,453),(453,554),(353,554)]
vert20=[(454,453),(554,453),(554,554),(454,554)]
vertfim=[(555,453),(555,554),(630,554),(630,453)]

#posicao das linhas pretas entre as casas
vertsi1=[(150,50),(150,150),(151,150),(151,50)]
verts12=[(251,50),(251,150),(252,150),(252,50)]
verts23=[(352,50),(352,150),(353,150),(353,50)]
verts34=[(453,50),(453,150),(454,150),(454,50)]
verts45=[(554,50),(554,150),(555,150),(555,50)]
verts56=[(655,50),(655,150),(656,150),(656,50)]
verts67=[(756,50),(756,150),(757,150),(757,50)]
verts78=[(757,150),(857,150),(857,151),(757,151)]
verts89=[(757,251),(857,251),(857,252),(757,252)]
verts910=[(756,252),(757,252),(757,352),(756,352)]
verts1011=[(655,252),(656,252),(656,352),(655,352)]
verts1112=[(554,252),(555,252),(555,352),(554,352)]
verts1213=[(453,252),(454,252),(454,352),(453,352)]
verts1314=[(352,252),(353,252),(353,353),(352,353)]
verts1415=[(251,252),(252,252),(252,352),(251,352)]
verts1516=[(151,352),(251,352),(251,353),(151,353)]
verts1617=[(151,452),(251,452),(251,453),(151,453)]
verts1718=[(251,453),(252,453),(252,554),(251,554)]
verts1819=[(352,453),(354,252+201),(354,353+201),(352,353+201)]
verts1920=[(453,453),(454,453),(454,555),(453,555)]
verts20fim=[(554,453),(556,453),(556,555),(554,555)]

#textos das casas
    #casa inicial
textini=font.render('Início',True,(0,0,0))
xini=80 
yini=90 

    #casa 1
text1=font.render('1',True,(0,0,0))
x1=151+42
y1=90

    #casa 2
text2=font.render('2',True,(0,0,0))
x2=252+42
y2=y1
    #casa 3
text3=font.render('3',True,(0,0,0))
x3=353+42
y3=y1
    #casa 4
text4=font.render('4',True,(0,0,0))
x4=454+42
y4=y1
    #casa 5 
text5=fontt.render('VOLTE',True,(255,0,0))
x5=580
y5=90
text5s=fontt.render('2 CASAS',True,(255,0,0))
x5s=575
y5s=105

    #casa 6
text6=font.render('6',True,(0,0,0))
x6=656+42
y6=y1

    #casa 7
text7=font.render('7',True,(0,0,0))
x7=757+42
y7=y1
    #casa 8 
text8=fontt.render('AVANCE',True,(255,0,0))
x8=775
y8=190
text8s=fontt.render('3 CASAS',True,(255,0,0))
x8s=774
y8s=205

    #casa 9
text9=font.render('9',True,(0,0,0))
x9=757+42
y9=251+40

    #casa 10
text10=font.render('10',True,(0,0,0))
x10=656+37
y10=y9
    #casa 11
text11=font.render('11',True,(0,0,0))
x11=555+37
y11=y9
    #casa 12
text12=font.render('12',True,(0,0,0))
x12=454+37
y12=y9
    #casa 13
text13=font.render('13',True,(0,0,0))
x13=353+37
y13=y9
    #casa 14
text14=font.render('14',True,(0,0,0))
x14=252+37
y14=252+37

    #casa 15
text15=fontt.render('AVANCE',True,(255,0,0))
x15=161+8
y15=242+46
text15s=fontt.render('2 CASAS',True,(255,0,0))
x15s=161+8
y15s=301+8

    #casa 16
text16=font.render('16',True,(0,0,0))
x16=151+37
y16=352+37

    #casa 17
text17=font.render('17',True,(0,0,0))
x17=151+37
y17=453+37

    #casa 18
text18=font.render('18',True,(0,0,0))
x18=252+37
y18=y17

    #casa 19
text19=font.render('19',True,(0,0,0))
x19=353+37
y19=y17

    #casa 20
text20=fontt.render('VOLTE PARA',True,(255,0,0))
x20=420+37
y20=y17
text20s=fontt.render('O INICIO',True,(255,0,0))
x20s=440+37
y20s=473+37

    #casa final
textfim=font.render('Fim',True,(0,0,0))
xfim=555+18
yfim=y17

#numero resultado do dado
textdado1=fontdado.render('DADO:',True,(255,0,0))

#clock
clock=pygame.time.Clock()
FPS = 60

#funcoes
def tela_de_instrucoes(tela):
    clock = pygame.time.Clock()
    #imagem
    background = pygame.image.load(path.join(pasta_img, 'imagem1.jpg')).convert()
    background_rect = background.get_rect()
    #codigo jogo
    jogando_i = True
    while jogando_i:
        clock.tick(FPS)
        #eventos
        for event in pygame.event.get():
            #fechar o jogo
            if event.type == pygame.QUIT:
                condicao = fim
                jogando_i = False
            #ir para proxima fase
            if event.type == pygame.KEYDOWN:
                condicao = jogo
                jogando_i = False
        tela.fill((0,0,0))
        #desenha background
        tela.blit(background, background_rect)
        pygame.display.flip()
    return condicao

#jogo
def tela_jogo(tela):
    #valor a ser impresso na tela
    DADO=0
    #casas andadas pelos participantes
    contador=0
    contador_bot_1=0
    contador_bot_2=0
    #define quem comeca jogando
    i='jogador'
    #define quem venceu
    venceu=False
    perdeu=False
    #loop principal
    game = True
    while game==True:
        clock.tick(FPS)
        #bot2 posicoes
        if contador_bot_2==0:
            posi_bot_2[0]=101
            posi_bot_2[1]=100
        if contador_bot_2==1:
            posi_bot_2[0]=2*101
            posi_bot_2[1]=100  
        if contador_bot_2==2:
            posi_bot_2[0]=3*101
            posi_bot_2[1]=100
        if contador_bot_2==3: 
            posi_bot_2[0]=4*101
            posi_bot_2[1]=100
        if contador_bot_2==4:
            posi_bot_2[0]=5*101
            posi_bot_2[1]=100
        if contador_bot_2==5:
            posi_bot_2[0]=4*101
            posi_bot_2[1]=100 
        if contador_bot_2==6:
            posi_bot_2[0]=7*101
            posi_bot_2[1]=100
        if contador_bot_2==7:
            posi_bot_2[0]=808
            posi_bot_2[1]=100
        if contador_bot_2==8:
            posi_bot_2[1]=100
            posi_bot_2[0]=606
        if contador_bot_2==9:
            posi_bot_2[0]=808
            posi_bot_2[1]=302
        if contador_bot_2==10:
            posi_bot_2[0]=707
            posi_bot_2[1]=302
        if contador_bot_2==11:
            posi_bot_2[0]=606
            posi_bot_2[1]=302
        if contador_bot_2==12:
            posi_bot_2[0]=505
            posi_bot_2[1]=302
        if contador_bot_2==13:
            posi_bot_2[0]=404
            posi_bot_2[1]=302
        if contador_bot_2==14:
            posi_bot_2[0]=303
            posi_bot_2[1]=302
        if contador_bot_2==15:
            posi_bot_2[0]=202 
            posi_bot_2[1]=504 
        if contador_bot_2==16:
            posi_bot_2[0]=202
            posi_bot_2[1]=403
        if contador_bot_2==17:
            posi_bot_2[0]=202
            posi_bot_2[1]=504
        if contador_bot_2==18:
            posi_bot_2[0]=303
            posi_bot_2[1]=504
        if contador_bot_2==19:
            posi_bot_2[0]=404
            posi_bot_2[1]=504
        if contador_bot_2==20:
            posi_bot_2[0]=100 
            posi_bot_2[1]=100 
            contador_bot_2-=20
        if contador_bot_2>21:
            contador_bot_2=21
        if contador_bot_2==21:
            posi_bot_2[0]=591
            posi_bot_2[1]=504
            #define que o jogador perdeu
            perdeu=True
        #bot1 posicoes
        if contador_bot_1==0:
            posi_bot_1[0]=101
            posi_bot_1[1]=100
        if contador_bot_1==1:
            posi_bot_1[0]=2*101
            posi_bot_1[1]=100  
        if contador_bot_1==2:
            posi_bot_1[0]=3*101
            posi_bot_1[1]=100
        if contador_bot_1==3: 
            posi_bot_1[0]=4*101
            posi_bot_1[1]=100
        if contador_bot_1==4:
            posi_bot_1[0]=5*101
            posi_bot_1[1]=100
        if contador_bot_1==5:
            posi_bot_1[0]=4*101
            posi_bot_1[1]=100 
        if contador_bot_1==6:
            posi_bot_1[0]=7*101
            posi_bot_1[1]=100
        if contador_bot_1==7:
            posi_bot_1[0]=808
            posi_bot_1[1]=100
        if contador_bot_1==8:
            posi_bot_1[1]=100
            posi_bot_1[0]=606
        if contador_bot_1==9:
            posi_bot_1[0]=808
            posi_bot_1[1]=302
        if contador_bot_1==10:
            posi_bot_1[0]=707
            posi_bot_1[1]=302
        if contador_bot_1==11:
            posi_bot_1[0]=606
            posi_bot_1[1]=302
        if contador_bot_1==12:
            posi_bot_1[0]=505
            posi_bot_1[1]=302
        if contador_bot_1==13:
            posi_bot_1[0]=404
            posi_bot_1[1]=302
        if contador_bot_1==14:
            posi_bot_1[0]=303
            posi_bot_1[1]=302
        if contador_bot_1==15:
            posi_bot_1[0]=202 
            posi_bot_1[1]=504 
        if contador_bot_1==16:
            posi_bot_1[0]=202
            posi_bot_1[1]=403
        if contador_bot_1==17:
            posi_bot_1[0]=202
            posi_bot_1[1]=504
        if contador_bot_1==18:
            posi_bot_1[0]=303
            posi_bot_1[1]=504
        if contador_bot_1==19:
            posi_bot_1[0]=404
            posi_bot_1[1]=504
        if contador_bot_1==20:
            posi_bot_1[0]=100 
            posi_bot_1[1]=100 
            contador_bot_1-=20
        if contador_bot_1>21:
            contador_bot_1=21
        if contador_bot_1==21:
            posi_bot_1[0]=591
            posi_bot_1[1]=504
            #define que o jogador perdeu
            perdeu=True
        #jogador posicoes
        if contador==0:
            posi_joga[0]=101
            posi_joga[1]=100
        if contador==1:
            posi_joga[0]=2*101
            posi_joga[1]=100  
        if contador==2:
            posi_joga[0]=3*101
            posi_joga[1]=100
        if contador==3: 
            posi_joga[0]=4*101
            posi_joga[1]=100
        if contador==4:
            posi_joga[0]=5*101
            posi_joga[1]=100
        if contador==5:
            posi_joga[0]=4*101
            posi_joga[1]=100 
        if contador==6:
            posi_joga[0]=7*101
            posi_joga[1]=100
        if contador==7:
            posi_joga[0]=808
            posi_joga[1]=100
        if contador==8:
            posi_joga[1]=100
            posi_joga[0]=606
        if contador==9:
            posi_joga[0]=808
            posi_joga[1]=302
        if contador==10:
            posi_joga[0]=707
            posi_joga[1]=302
        if contador==11:
            posi_joga[0]=606
            posi_joga[1]=302
        if contador==12:
            posi_joga[0]=505
            posi_joga[1]=302
        if contador==13:
            posi_joga[0]=404
            posi_joga[1]=302
        if contador==14:
            posi_joga[0]=303
            posi_joga[1]=302
        if contador==15:
            posi_joga[0]=202 
            posi_joga[1]=504 
        if contador==16:
            posi_joga[0]=202
            posi_joga[1]=403
        if contador==17:
            posi_joga[0]=202
            posi_joga[1]=504
        if contador==18:
            posi_joga[0]=303
            posi_joga[1]=504
        if contador==19:
            posi_joga[0]=404
            posi_joga[1]=504
        if contador==20:
            posi_joga[0]=100 
            posi_joga[1]=100 
            contador-=20
        if contador>21:
            contador=21
        if contador==21:
            posi_joga[0]=591
            posi_joga[1]=504
            #define que o jogador venceu
            venceu=True
        #verifica eventos
        for event in pygame.event.get():
            #jogador comeca
            if i == 'jogador':
                #fechar o jogo
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game=False
                #avancar no jogo
                if event.type == pygame.KEYDOWN:  
                    if event.key ==pygame.K_SPACE:
                        #sorteia numero de casas andadas
                        dado=randint(1,4)
                        DADO=dado
                        #anda as casas
                        contador+=dado
                        #verifica em qual casa esta
                        if contador==1:
                            #roda o jogo
                            jog1=CASA1(window)
                            if jog1=='repita':
                                contador-=dado  
                        if contador==2:
                            #roda o jogo
                            jog2=CASA2(window)
                            #verifica se o desafio foi superado
                            if jog2=='repita':
                                contador-=dado
                        if contador==3: 
                            #roda o jogo
                            jogF1=FORCA(window)
                            #verifica se o desafio foi superado
                            if jogF1!='continue':
                                contador-=dado
                        if contador==4:
                            #roda o jogo
                            jog3=CASA3(window)
                            #verifica se o desafio foi superado
                            if jog3=='repita':
                                contador-=dado
                        if contador==5:
                            #volta duas casas
                            contador-=2 
                        if contador==6:
                            #roda o jogo
                            #roda o jogo
                            jogJ1=JOKENPO(window)
                            #verifica se o desafio foi superado
                            if jogJ1!='continue':
                                contador-=dado
                        if contador==7:
                            #roda o jogo
                            jog4=CASA4(window)
                            #verifica se o desafio foi superado
                            if jog4=='repita':
                                contador-=dado
                        if contador==8:
                            #avanca tres casas
                            contador+=3
                        if contador==9:
                            #roda o jogo
                            jogC1=CESTA(window)
                            #verifica se o desafio foi superado
                            if jogC1!='continue':
                                contador-=dado
                        if contador==10:
                            #roda o jogo
                            jog5=CASA5(window)
                            #verifica se o desafio foi superado
                            if jog5=='repita':
                                contador-=dado
                        if contador==11:
                            #roda o jogo
                            jogF2=FORCA(window)
                            #verifica se o desafio foi superado
                            if jogF2!='continue':
                                contador-=dado
                        if contador==12:
                            #roda o jogo
                            jog6=CASA6(window)
                            #verifica se o desafio foi superado
                            if jog6=='repita':
                                contador-=dado
                        if contador==13:
                            #roda o jogo
                            jog7=CASA7(window)
                            #verifica se o desafio foi superado
                            if jog7=='repita':
                                contador-=dado
                        if contador==14:
                            #roda o jogo
                            jog8=CASA8(window)
                            #verifica se o desafio foi superado
                            if jog8=='repita':
                                contador-=dado
                        if contador==15:
                            #roda o jogo
                            jog9=CASA2(window)
                            #verifica se o desafio foi superado
                            if jog9=='repita':
                                contador-=dado
                        if contador==16:
                            #roda o jogo
                            jog10=CASA6(window)
                            #verifica se o desafio foi superado
                            if jog10=='repita':
                                contador-=dado
                        if contador==17:
                            #roda o jogo
                            jogJ2=JOKENPO(window)
                            #verifica se o desafio foi superado
                            if jogJ2!='continue':
                                contador-=dado
                        if contador==18:
                            #roda o jogo
                            jog11=CASA3(window)
                            #verifica se o desafio foi superado
                            if jog11=='repita':
                                contador-=dado
                        if contador==19:
                            #roda o jogo
                            jogC2=CESTA(window)
                            #verifica se o desafio foi superado
                            if jogC2!='continue':
                                contador-=dado
                        if contador==20:
                            #volta para o inicio
                            contador-=20
                        i='bot1'
            if i == 'bot1':
                #fecha o jogo
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game=False
                    #verifica eventos
                if event.type == pygame.KEYDOWN:  
                    if event.key ==pygame.K_x:
                        #bot 1
                        #numero de casas andadas
                        dado_bot_1=randint(1,4)
                        #chance do bot vencer o desafio
                        chance_bot_1=randint(1,11)    
                        DADO=dado_bot_1
                        #verifica se o bot venceu o desafio
                        if 0<chance_bot_1<7:
                            #anda casas
                            contador_bot_1+=dado_bot_1    
                            #vcasas especiais
                            if contador_bot_1==5:
                                contador_bot_1-=2 
                            if contador_bot_1==8:
                                contador_bot_1+=3
                            if contador_bot_1==15:
                                contador_bot_1+=2                                
                            if contador_bot_1==20:
                                contador_bot_1-=20

                             
                        #bot 2
                        #numero de casas andadas
                        dado_bot_2=randint(1,4)
                        #chance do bot vencer o desafio
                        chance_bot_2=randint(1,11)    
                        DADO=dado_bot_2
                        #veerifica se ele venceu o desafio
                        if 0<chance_bot_2<7:
                            #anda as casas
                            contador_bot_2+=dado_bot_2    
                            #casas especiais
                            if contador_bot_2==5:
                                contador_bot_2-=2 
                            if contador_bot_2==8:
                                contador_bot_2+=3
                            if contador_bot_2==15:
                                contador_bot_2+=2                                
                            if contador_bot_2==20:
                                contador_bot_2-=20
                        i = 'jogador'
                       

        window.blit(background, (0, 0))

        #desenha casas
        pygame.draw.polygon(window, verde, vertfim)
        pygame.draw.polygon(window, cinza, vert20)
        pygame.draw.polygon(window, vermelho, vert19)
        pygame.draw.polygon(window, cinza, vert18)
        pygame.draw.polygon(window, vermelho, vert17)
        pygame.draw.polygon(window, cinza, vert16)
        pygame.draw.polygon(window, cinza, vert15)
        pygame.draw.polygon(window, cinza, vert14)
        pygame.draw.polygon(window, cinza, vert13)
        pygame.draw.polygon(window, cinza, vert12)
        pygame.draw.polygon(window, vermelho, vert11)
        pygame.draw.polygon(window, cinza, vert10)
        pygame.draw.polygon(window, vermelho, vert9)       
        pygame.draw.polygon(window, cinza, vert8)
        pygame.draw.polygon(window, cinza, vert7)
        pygame.draw.polygon(window, vermelho, vert6)
        pygame.draw.polygon(window, cinza, vert5)
        pygame.draw.polygon(window, cinza, vert4)
        pygame.draw.polygon(window, vermelho, vert3)
        pygame.draw.polygon(window, cinza, vert2)
        pygame.draw.polygon(window, cinza, vert1)
        pygame.draw.polygon(window, verde, vertini)

        #desenha linhas
        pygame.draw.polygon(window, preto, vertsi1)
        pygame.draw.polygon(window, preto, verts12)
        pygame.draw.polygon(window, preto, verts23)
        pygame.draw.polygon(window, preto, verts34)
        pygame.draw.polygon(window, preto, verts45)
        pygame.draw.polygon(window, preto, verts56)
        pygame.draw.polygon(window, preto, verts67)
        pygame.draw.polygon(window, preto, verts78)
        pygame.draw.polygon(window, preto, verts89)
        pygame.draw.polygon(window, preto, verts910)
        pygame.draw.polygon(window, preto, verts1011)
        pygame.draw.polygon(window, preto, verts1112)
        pygame.draw.polygon(window, preto, verts1213)
        pygame.draw.polygon(window, preto, verts1314)
        pygame.draw.polygon(window, preto, verts1415)
        pygame.draw.polygon(window, preto, verts1516)
        pygame.draw.polygon(window, preto, verts1617)
        pygame.draw.polygon(window, preto, verts1718)
        pygame.draw.polygon(window, preto, verts1819)
        pygame.draw.polygon(window, preto, verts1920)
        pygame.draw.polygon(window, preto, verts20fim)
        
        #desenha textos
        window.blit(textini, (xini,yini))
        window.blit(text1, (x1,y1))
        window.blit(text2, (x2,y2))
        window.blit(text3, (x3,y3))
        window.blit(text4, (x4,y4))
        window.blit(text5, (x5,y5))
        window.blit(text5s, (x5s,y5s))
        window.blit(text6, (x6,y6))
        window.blit(text7, (x7,y7))
        window.blit(text8, (x8,y8))
        window.blit(text8s, (x8s,y8s))
        window.blit(text9, (x9,y9))
        window.blit(text10, (x10,y10))
        window.blit(text11, (x11,y11))
        window.blit(text12, (x12,y12))
        window.blit(text13, (x13,y13))
        window.blit(text14, (x14,y14))
        window.blit(text15, (x15,y15))
        window.blit(text15s, (x15s,y15s))
        window.blit(text16, (x16,y16))
        window.blit(text17, (x17,y17))
        window.blit(text18, (x18,y18))
        window.blit(text19, (x19,y19))
        window.blit(text20, (x20,y20))
        window.blit(text20s, (x20s,y20s))
        window.blit(textfim, (xfim,yfim))
        window.blit(textdado1, (700,500))
        window.blit(fontdado.render(str(DADO),True,(255,0,0)), (920,500))

        #jogadores
            #peao
        pygame.draw.circle(window,azul,posi_joga,27)
            #bot1
        pygame.draw.circle(window,branco,posi_bot_1,25)
            #bot2
        pygame.draw.circle(window,preto,posi_bot_2,23)
        
        #verifica vencedor
        if perdeu==True:
            resultado_jogo = pygame.font.SysFont(None,180).render('Voce perdeu', True, (roxo))     
            local_resultado_jogo=resultado_jogo.get_rect()
            local_resultado_jogo.midtop=(resultado_jogo_coordenadas)
            window.blit(resultado_jogo, local_resultado_jogo)  
        if venceu==True:
            resultado_jogo = pygame.font.SysFont(None,180).render('Voce venceu', True, (roxo))     
            local_resultado_jogo=resultado_jogo.get_rect()
            local_resultado_jogo.midtop=(resultado_jogo_coordenadas)
            window.blit(resultado_jogo, local_resultado_jogo)  
        #update
        pygame.display.update() 

#roda o jogo
condicao = instrucao
while condicao != fim:
    if condicao == instrucao:
        condicao = tela_de_instrucoes(window)
    elif condicao == jogo:
        condicao = tela_jogo(window)
    else:
        condicao = fim
#encerra o jogo
pygame.quit()
