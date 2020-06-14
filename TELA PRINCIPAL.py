from random import randint
import pygame
from CASA1 import CASA1
from CASA2 import CASA2
from CASA3 import CASA3
from CASA4 import CASA4
from CASA5 import CASA5
from CASA6 import CASA6
from CASA7 import CASA7
from CASA8 import CASA8

pygame.init()
pygame.mixer.init()
altura=600
largura=1000
window=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('JOGO')
background = pygame.image.load("telainicialpygame.jpg").convert()
#########################################################################
cor=(0,0,255)
cor1=(0,200,0)
cors=(0,0,0)
core=(127,127,127)
cormg=(230,170,0)
##########################################################################
METEOR_WIDTH = 50
METEOR_HEIGHT = 38
meteor_img = pygame.image.load('meteorBrown_med1.png').convert_alpha()
meteor_img_small = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT))
############################################################################
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
##############################################################################
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

#########################################################################
poscir=[100,100]
###############################################################
font= pygame.font.SysFont(None,36)
fontt= pygame.font.SysFont(None,23)
fontdado= pygame.font.SysFont(None,90)
textini=font.render('Início',True,(0,0,0))
xini=80 
yini=90 
textini=font.render('Início',True,(0,0,0))
xini=80 
yini=90
text1=font.render('1',True,(0,0,0))
x1=151+42
y1=90
text2=font.render('2',True,(0,0,0))
x2=252+42
text3=font.render('3',True,(0,0,0))
x3=353+42
text4=font.render('4',True,(0,0,0))
x4=454+42
text5=fontt.render('VOLTE',True,(255,0,0))
x5=580
y5=90
text5s=fontt.render('2 CASAS',True,(255,0,0))
x5s=575
y5s=105
text6=font.render('6',True,(0,0,0))
x6=656+42
text7=font.render('7',True,(0,0,0))
x7=757+42
text8=fontt.render('AVANCE',True,(255,0,0))
x8=775
y8=190
text8s=fontt.render('3 CASAS',True,(255,0,0))
x8s=774
y8s=205
text9=font.render('9',True,(0,0,0))
x9=757+42
y9=251+40
text10=font.render('10',True,(0,0,0))
x10=656+37
text11=font.render('11',True,(0,0,0))
x11=555+37
text12=font.render('12',True,(0,0,0))
x12=454+37
text13=font.render('13',True,(0,0,0))
x13=353+37
text14=font.render('14',True,(0,0,0))
x14=252+37
y14=252+37
text15=fontt.render('AVANCE',True,(255,0,0))
x15=161+8
y15=242+46
text15s=fontt.render('2 CASAS',True,(255,0,0))
x15s=161+8
y15s=301+8
text16=font.render('16',True,(0,0,0))
x16=151+37
y16=352+37
text17=font.render('17',True,(0,0,0))
x17=151+37
y17=453+37
text18=font.render('18',True,(0,0,0))
x18=252+37
y18=453+37
text19=font.render('19',True,(0,0,0))
x19=353+37
y19=453+37
text20=fontt.render('VOLTE PARA',True,(255,0,0))
x20=420+37
y20=453+37
text20s=fontt.render('O INICIO',True,(255,0,0))
x20s=440+37
y20s=473+37
textI=fontt.render('INÍCIO', True,(255,0,0))
x15i=353+30
y15i=453+60
textfim=font.render('Fim',True,(0,0,0))
xfim=555+18
yfim=453+39
textdado1=fontdado.render('DADO:',True,(255,0,0))
DADO=0
#######################################################
clock=pygame.time.Clock()
FPS = 60
######################################################
class Meteoro(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image=img
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y=randint(20,580)
        self.speedx=randint(30,60)
        self.speedy=0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right < 0 or self.rect.left > largura: 
            self.rect.x =0
            self.rect.y = randint(20,580)
            self.speedx = randint(30,60)
            self.speedy = 0
meteoro1=Meteoro(meteor_img)
meteoro2=Meteoro(meteor_img)
game = True
contador=0
flow='continue'
while game==True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game=False
        if event.type == pygame.KEYDOWN:  
            if event.key ==pygame.K_SPACE and flow=='continue':
                dado=randint(1,4)
                DADO=dado
                contador+=dado
                if contador==1:
                    poscir[0]=2*101
                    poscir[1]=100 
                    CASA1(window)  
                if contador==2:
                    poscir[0]=3*101
                    poscir[1]=100
                    CASA2(window) 
                if contador==3:
                    poscir[0]=4*101
                    poscir[1]=100
                if contador==4:
                    poscir[0]=5*101
                    poscir[1]=100
                    CASA3(window)
                if contador==5:
                    poscir[0]=4*101
                    poscir[1]=100
                    contador-=2 
                if contador==6:
                    poscir[0]=7*101
                    poscir[1]=100
                if contador==7:
                    poscir[0]=808
                    poscir[1]=100
                    CASA4(window)
                if contador==8:
                    poscir[1]=100
                    poscir[0]=606
                    contador+=3
                if contador==9:
                    poscir[0]=808
                    poscir[1]=302
                if contador==10:
                    poscir[0]=707
                    poscir[1]=302
                    CASA5(window)
                if contador==11:
                    poscir[0]=606
                    poscir[1]=302
                if contador==12:
                    poscir[0]=505
                    poscir[1]=302
                    CASA6(window)
                if contador==13:
                    poscir[0]=404
                    poscir[1]=302
                    CASA7(window)
                if contador==14:
                    poscir[0]=303
                    poscir[1]=302
                    CASA8(window)
                if contador==15:
                    poscir[0]=202 
                    poscir[1]=504 
                    CASA2(window)
                if contador==16:
                    poscir[0]=202
                    poscir[1]=403
                    CASA6(window)
                if contador==17:
                    poscir[0]=202
                    poscir[1]=504
                if contador==18:
                    poscir[0]=303
                    poscir[1]=504
                    CASA3(window)
                if contador==19:
                    poscir[0]=404
                    poscir[1]=504
                if contador==20:
                    poscir[0]=100 
                    poscir[1]=100 
                    contador-=20
                if contador>21:
                    contador=21
                if contador==21:
                    poscir[0]=591
                    poscir[1]=504 
            if event.key == pygame.K_SPACE and flow == 'repita':
                if contador==1:
                    poscir[0]=2*101
                    poscir[1]=100 
                    CASA1(window)  
                if contador==2:
                    poscir[0]=3*101
                    poscir[1]=100
                    CASA2(window) 
                if contador==3:
                    poscir[0]=4*101
                    poscir[1]=100
                if contador==4:
                    poscir[0]=5*101
                    poscir[1]=100
                    CASA3(window)
                if contador==5:
                    poscir[0]=4*101
                    poscir[1]=100
                    contador-=2 
                if contador==6:
                    poscir[0]=7*101
                    poscir[1]=100
                if contador==7:
                    poscir[0]=808
                    poscir[1]=100
                    CASA4(window)
                if contador==8:
                    poscir[1]=100
                    poscir[0]=606
                    contador+=3
                if contador==9:
                    poscir[0]=808
                    poscir[1]=302
                if contador==10:
                    poscir[0]=707
                    poscir[1]=302
                    CASA5(window)
                if contador==11:
                    poscir[0]=606
                    poscir[1]=302
                if contador==12:
                    poscir[0]=505
                    poscir[1]=302
                    CASA6(window)
                if contador==13:
                    poscir[0]=404
                    poscir[1]=302
                    CASA7(window)
                if contador==14:
                    poscir[0]=303
                    poscir[1]=302
                    CASA8(window)
                if contador==15:
                    poscir[0]=202 
                    poscir[1]=504 
                    CASA2(window)
                if contador==16:
                    poscir[0]=202
                    poscir[1]=403
                    CASA6(window)
                if contador==17:
                    poscir[0]=202
                    poscir[1]=504
                if contador==18:
                    poscir[0]=303
                    poscir[1]=504
                    CASA3(window)
                if contador==19:
                    poscir[0]=404
                    poscir[1]=504
                if contador==20:
                    poscir[0]=100 
                    poscir[1]=100 
                    contador-=20
                if contador>21:
                    contador=21
                if contador==21:
                    poscir[0]=591
                    poscir[1]=504 
    meteoro1.update()
    meteoro2.update()
    window.blit(background, (0, 0))
    window.blit(meteoro1.image, meteoro1.rect)
    window.blit(meteoro2.image, meteoro2.rect)
    ####################################################
    pygame.draw.polygon(window, cor1, vertfim)
    pygame.draw.polygon(window, cor, vert20)
    pygame.draw.polygon(window, cormg, vert19)
    pygame.draw.polygon(window, cor, vert18)
    pygame.draw.polygon(window, cormg, vert17)
    pygame.draw.polygon(window, cor, vert16)
    pygame.draw.polygon(window, cor, vert15)
    pygame.draw.polygon(window, cor, vert14)
    pygame.draw.polygon(window, cor, vert13)
    pygame.draw.polygon(window, cor, vert12)
    pygame.draw.polygon(window, cormg, vert11)
    pygame.draw.polygon(window, cor, vert10)
    pygame.draw.polygon(window, cormg, vert9)       
    pygame.draw.polygon(window, cor, vert8)
    pygame.draw.polygon(window, cor, vert7)
    pygame.draw.polygon(window, cormg, vert6)
    pygame.draw.polygon(window, cor, vert5)
    pygame.draw.polygon(window, cor, vert4)
    pygame.draw.polygon(window, cormg, vert3)
    pygame.draw.polygon(window, cor, vert2)
    pygame.draw.polygon(window, cor, vert1)
    ######################################################
    pygame.draw.polygon(window, cor1, vertini)
    pygame.draw.polygon(window, cors, vertsi1)
    pygame.draw.polygon(window, cors, verts12)
    pygame.draw.polygon(window, cors, verts23)
    pygame.draw.polygon(window, cors, verts34)
    pygame.draw.polygon(window, cors, verts45)
    pygame.draw.polygon(window, cors, verts56)
    pygame.draw.polygon(window, cors, verts67)
    pygame.draw.polygon(window, cors, verts78)
    pygame.draw.polygon(window, cors, verts89)
    pygame.draw.polygon(window, cors, verts910)
    pygame.draw.polygon(window, cors, verts1011)
    pygame.draw.polygon(window, cors, verts1112)
    pygame.draw.polygon(window, cors, verts1213)
    pygame.draw.polygon(window, cors, verts1314)
    pygame.draw.polygon(window, cors, verts1415)
    pygame.draw.polygon(window, cors, verts1516)
    pygame.draw.polygon(window, cors, verts1617)
    pygame.draw.polygon(window, cors, verts1718)
    pygame.draw.polygon(window, cors, verts1819)
    pygame.draw.polygon(window, cors, verts1920)
    pygame.draw.polygon(window, cors, verts20fim)
    
    #############################################################
    window.blit(textini, (xini,yini))
    window.blit(text1, (x1,y1))
    window.blit(text2, (x2,y1))
    window.blit(text3, (x3,y1))
    window.blit(text4, (x4,y1))
    window.blit(text5, (x5,y5))
    window.blit(text5s, (x5s,y5s))
    window.blit(text6, (x6,y1))
    window.blit(text7, (x7,y1))
    window.blit(text8, (x8,y8))
    window.blit(text8s, (x8s,y8s))
    window.blit(text9, (x9,y9))
    window.blit(text10, (x10,y9))
    window.blit(text11, (x11,y9))
    window.blit(text12, (x12,y9))
    window.blit(text13, (x13,y9))
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
    #############################################################
    pygame.draw.circle(window,core,poscir,25)
    pygame.display.update() 
pygame.quit()