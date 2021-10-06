import pygame
import random
import time
pygame.init()

white=(225,225,225)
black=(0,0,0)
lightgrey=(60,179,113,0.4)
blue=(0,0,225)
smallfont=pygame.font.SysFont('Segoe Print',22)
#largefont=pygame.font.SysFont('Segoe Print',44)
display_width=60
display_height=600
highway=pygame.image.load('highway.png')
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('game')
clock=pygame.time.Clock()



def button(txt,color,buttonx,buttony,buttonwidth,buttonheight,active_color,inactive_color,action):
    global start
    curser=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if (buttonx+buttonwidth>curser[0] and curser[0]>buttonx) and buttony+buttonheight>curser[1]>buttony:
        pygame.draw.rect(gameDisplay,active_color,[buttonx,buttony,buttonwidth,buttonheight])
        if click[0]==1:
            if action=="Play":
                message("starting",black,0,"smallfont")
                time.sleep(3)
                start=False
                Gameloop()
                
    else:
        pygame.draw.rect(gameDisplay,inactive_color,[buttonx,buttony,buttonwidth,buttonheight])
    message_button(txt,color,buttonx,buttony,buttonwidth,buttonheight)

def score(scor):
    text=smallfont.render("Score: "+str(scor),True,black)
    gameDisplay.blit(text,[10,0])



                
def text(txt,color,size):
    if size=="smallfont":
        textsurface=smallfont.render(txt,True,color)
    #if size=="largefont":
        #textsurface=largefont.render(txt,True,color)
    return textsurface,textsurface.get_rect()

def message_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="smallfont"):
    textSurf,textRect=text(msg,color,size)
    textRect.center=(buttonx+(buttonwidth/2) ,buttony+(buttonheight/2))
    gameDisplay.blit(textSurf,textRect)

def message(msg,color,ydisplace=0,size='smallfont'):
    textSurf,textRect=text(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+ydisplace
    gameDisplay.blit(textSurf,textRect)

def start():
    global start
    start=True
    gameDisplay.fill(white)
    message("Bullet",black,-170,size="smallfont")
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Play",black,0,300,60,50,lightgrey,blue,action="Play")
        pygame.display.update()
        clock.tick(7)

def Gameloop():
    gameexit= False
    gameover=False
    global score
    rand_red=random.randint(0,225)
    rand_green=random.randint(0,225)
    rand_blue=random.randint(0,225)
    random_color=(rand_red,rand_green,rand_blue)
    x=22
    y=550
    x_change=0

    y_car=[0,0,0,0,0,0,0,0,0,0]
    x_car=[0,0,0,0,0,0,0,0,0,0]
    y_cars=0
    x_cars=0
    for i in range(10):
        randy=random.randint(100,600)
        if randy%3==0:
            x_cars=1
        elif randy%3==1:
            x_cars=23
        else:
            x_cars=43
        y_car[i]=y_cars
        x_car[i]=x_cars
        y_cars+=-randy
    
    while not gameexit:
        if gameover==True:
            message("Over",random_color,-80,'smallfont')
        while gameover==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            button("Play Again",black,0,300,60,50,lightgrey,white,action="Play")
            pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-21
                if event.key==pygame.K_RIGHT:
                    x_change=21
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    x_change=0
                if event.key==pygame.K_RIGHT:
                    x_change=0
        gameDisplay.fill(white)
        if x>=0 and x<=43:
            x+=x_change
        else:
            if x<0:
                x=1
            elif x>43:
                x=43

        gameDisplay.blit(highway,(0,0))
        pygame.draw.line(gameDisplay,white,(18,0),(18,display_height),3)
        pygame.draw.line(gameDisplay,white,(39,0),(39,display_height),3)
        for i in range(10):
            y_car[i]+=20
            pygame.draw.rect(gameDisplay,random_color,[x_car[i],y_car[i],10,10])
        pygame.draw.rect(gameDisplay,blue,[x,y,10,10])


        if y_car[9]>display_height:
            y_car=[0,0,0,0,0,0,0,0,0,0]
            x_car=[0,0,0,0,0,0,0,0,0,0]
            y_cars=0
            x_cars=0
            for i in range(10):
                randy=random.randint(100,600)
                if randy%3==0:
                    x_cars=1
                elif randy%3==1:
                    x_cars=22
                else:
                    x_cars=43
                y_car[i]=y_cars
                x_car[i]=x_cars
                y_cars+=-randy

        for i in range(10):
            if y_car[i]>=540 and y_car[i]<=560:
                if x_car[i]>=x-10 and x_car[i]<=x+10:
                    gameover=True


        pygame.display.update()
        clock.tick(20)
start()
Gameloop()
pygame.quit()
quit()






