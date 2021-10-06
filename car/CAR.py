import pygame
import random
import time
pygame.init()
#sound=pygame.mixer.Sound('eatapple.wav')
white=(225,225,225)
black=(0,0,0)
lightgrey=(60,179,113,0.4)
blue=(0,0,225)
smallfont=pygame.font.SysFont('Segoe Print',36)
#largefont=pygame.font.SysFont('Segoe Print',44)
display_width=270
display_height=600
highway=pygame.image.load('highway.png')
Car=pygame.image.load('car.png')
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
                #message("starting",black,0,"smallfont")
                #time.sleep(3)
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
    message("Cars",black,-170,size="smallfont")
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    start=False
                    Gameloop()
        button("Play",black,0,300,270,50,lightgrey,blue,action="Play")
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
    x=105
    y=500
    x_change=0
    speed=1
    speed_highway=7
    flag=0
    scor=0
    y_highway=[0,0,0,0,0]
    y_highways=0
    for i in range(5):
        
        y_highway[i]=y_highways
        y_highways+=-300


    y_car=[0,0,0,0,0,0,0,0,0,0]
    x_car=[0,0,0,0,0,0,0,0,0,0]
    y_cars=0
    x_cars=0
    for i in range(10):
        randy=random.randint(170,1000)
        if randy%3==0:
            x_cars=10
        elif randy%3==1:
            x_cars=105
        else:
            x_cars=200
        y_car[i]=y_cars
        x_car[i]=x_cars
        y_cars+=-randy
    
    while not gameexit:
        if gameover==True:
            message("Game Over",random_color,-80,'smallfont')
        while gameover==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        start=False
                        Gameloop()
            button("Play",black,0,300,270,50,lightgrey,blue,action="Play")
            #pygame.mixer.Sound.play(sound)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and x>=15:
                    x_change=-15
                if event.key==pygame.K_RIGHT:
                    x_change=15
                if event.key==pygame.K_UP:
                    speed=25
                    speed_highway=31
                    flag=1
                    #scor+=3
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or x<=0:
                    x_change=0
                if event.key==pygame.K_RIGHT:
                    x_change=0
                if event.key==pygame.K_UP:
                    speed=1
                    speed_highway=7
                    #scor+=1
                    flag=0
        gameDisplay.fill(white)
        if flag==1:
            scor+=6
        else:
            scor+=1
        gameDisplay.blit(highway,(0,0))
        if x>=-5 and x<=225:
            x+=x_change
        else:
            if x<0:
                x=-5
            elif x>222:
                x=225
        i=0
        for i in range(5):
            y_highway[i]+=speed_highway
            pygame.draw.rect(gameDisplay,white,[80,y_highway[i],15,100])
            pygame.draw.rect(gameDisplay,white,[175,y_highway[i],15,100])
        
        for i in range(10):
            y_car[i]+=speed
            #pygame.draw.rect(gameDisplay,random_color,[x_car[i],y_car[i],50,70])
            gameDisplay.blit(Car,(x_car[i],y_car[i]))
        gameDisplay.blit(Car,(x,y))




        if y_highway[2]>display_height:
            i=0
            y_highways=0
            for i in range(3):
                y_highways+=-300
                y_highway[i]=y_highways
        if y_highway[4]>display_height:
            i=3
            y_highways=0
            for i in range(3,5):
                y_highways+=-300
                y_highway[i]=y_highways
        if y_car[9]>display_height:
            y_car=[0,0,0,0,0,0,0,0,0,0]
            x_car=[0,0,0,0,0,0,0,0,0,0]
            y_cars=0
            x_cars=0
            for i in range(10):
                randy=random.randint(80,700)
                if randy%3==0:
                    x_cars=15
                elif randy%3==1:
                    x_cars=115
                else:
                    x_cars=215
                y_car[i]=y_cars
                x_car[i]=x_cars
                y_cars+=-randy
        for i in range(10):
            if y_car[i]>=410 and y_car[i]<=590:
                if x_car[i]>=x-50 and x_car[i]<=x+50:
                    gameover=True
        score(scor)
        pygame.display.update()
        clock.tick(25)
start()
Gameloop()
pygame.quit()
quit()






