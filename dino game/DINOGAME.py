import pygame
import random
import time
pygame.init()
white=(225,225,225)
rand_red=random.randint(175,200)
rand_green=random.randint(200,225)
rand_blue=random.randint(0,20)
random_color=(rand_red,rand_green,rand_blue)
black=(0,0,0)
lightgrey=(60,179,113,0.4)
red=(225,0,0)
smallfont=pygame.font.SysFont('Segoe Print',28)
largefont=pygame.font.SysFont('Segoe Print',64)
display_width=800
display_height=600
dino=pygame.image.load('dino.png')
tree=pygame.image.load('tree.png')
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('game')
clock=pygame.time.Clock()


def text(txt,color,size):
    if size=="smallfont":
        textsurface=smallfont.render(txt,True,color)
    if size=="largefont":
        textsurface=largefont.render(txt,True,color)
    return textsurface,textsurface.get_rect()

def message_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="smallfont"):
    textSurf,textRect=text(msg,color,size)
    textRect.center=(buttonx+(buttonwidth/2) ,buttony+(buttonheight/2))
    gameDisplay.blit(textSurf,textRect)

def message(msg,color,ydisplace=0,size='smallfont'):
    textSurf,textRect=text(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+ydisplace
    gameDisplay.blit(textSurf,textRect)


def button(txt,color,buttonx,buttony,buttonwidth,buttonheight,active_color,inactive_color,action):
    global start
    curser=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if (buttonx+buttonwidth>curser[0] and curser[0]>buttonx) and buttony+buttonheight>curser[1]>buttony:
        pygame.draw.rect(gameDisplay,active_color,[buttonx,buttony,buttonwidth,buttonheight])
        if click[0]==1:
            if action=="Play":
                #message("starting",random_color,0,size="smallfont")
                #time.sleep(3)
                start=False
                Gameloop()
                
    else:
        pygame.draw.rect(gameDisplay,inactive_color,[buttonx,buttony,buttonwidth,buttonheight])
    message_button(txt,color,buttonx,buttony,buttonwidth,buttonheight)

def score(scor):
    text=smallfont.render("Score: "+str(scor),True,black)
    gameDisplay.blit(text,[10,0])

def start():
    global start
    start=True
    gameDisplay.fill(white)
    message("Google Game",black,-170,"largefont")
    message("Press Space to jump",black,170,"smallfont")
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    Gameloop()
        button("Play",black,350,300,100,50,lightgrey,random_color,action="Play")
        pygame.display.update()
        clock.tick(7)

                





def Gameloop():
    gameexit= False
    gameover=False
    global score
    x=display_width
    list1=[0,0,0,0,0]
    for i in range(5):
        randx=random.randint(200,800)
        list1[i]=x
        x+=randx
    #randx=0
    scor=0
    flag=0
    x=800
    x_change=-15
    y1=450
    y1_change=0
    y1_changesq=0
    while not gameexit:
        if gameover==True:
            message("Game Over",red,-80,'largefont')
        while gameover==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        Gameloop()
            button("Play Again",black,300,300,200,50,lightgrey,white,action="Play")
            pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if y1==450:
                        y1_change=-35
                        y1_changesq=5
                        flag=1
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    flag=0

        y1_change+=y1_changesq
        y1+=y1_change
        if y1>=450:
            y1=450
            y1_change=0
            y1_changesq=0
        if flag==1:
            if y1==450:
                y1_change=-35
                y1_changesq=5


        for k in range(5):
            if list1[k]>=100  and list1[k]<=120:
                if y1>=400:
                    gameover=True


        gameDisplay.fill(random_color)
        pygame.draw.line(gameDisplay,black,(0,500),(800,500),5)
        gameDisplay.blit(dino,(100,y1))
        randx=random.randint(250,800)
        
        for j in range(5):
            list1[j]+=x_change
            gameDisplay.blit(tree,(list1[j],450))

        if list1[4]<=0:
            i=0
            x=random.randint(600,800)
            for i in range(5):
                randx=random.randint(500,800)
                list1[i]=x
                x+=randx
                #print(list1[i])for test

        scor+=1
        i=0
        for i in range(5):
            if list1[i]>=100 and list1[i]<=100-x_change: #so that score only increase one time
                scor+=30
                break
        score(scor)
        pygame.display.update()
        clock.tick(25)
start()
Gameloop()
pygame.quit()
quit()
