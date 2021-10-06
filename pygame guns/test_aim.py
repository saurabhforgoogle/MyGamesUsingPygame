import pygame
import random
import time
import os
pygame.init()

from pygame import mixer 
  
# Starting the mixer
mixer.init()
  
# Loading the song 
mixer.music.load(r"C:\Users\saurabh\Documents\Desktop\Projects\pygame\snake\pygame guns\m16.mp3")
  

white=(225,225,225)
black=(0,0,0)
red=(225,0,0,0.4)
green=(10,160,5)
shade=(255,30,255)
blue=(0,0,100)
display_width=1200
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
#background = pygame.Surface((display_width,display_height))

dot=pygame.image.load(r'C:\Users\saurabh\Documents\Desktop\Projects\pygame\snake\pygame guns\reddot.png').convert_alpha()
gun=pygame.image.load(r'C:\Users\saurabh\Documents\Desktop\Projects\pygame\snake\pygame guns\gun.png').convert_alpha()
scopes=pygame.image.load(r'C:\Users\saurabh\Documents\Desktop\Projects\pygame\snake\pygame guns\scope.png').convert_alpha()
#convert_alpha(dot)
background=pygame.image.load(r'C:\Users\saurabh\Documents\Desktop\Projects\pygame\snake\pygame guns\wallpaper.jpg').convert_alpha()
smallfont=pygame.font.SysFont('Segoe Print',28)
medfont=pygame.font.SysFont('Segoe Print',36)
largefont=pygame.font.SysFont('Segoe Print',64)

pygame.display.set_caption('game')
block=20
block_size=100
global start
global setting
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,25)

def setting():
    global setting
    global start
    setting=True
    gameDisplay.fill(white)
    while setting:
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(7)
def Modes():
    global choice
    global mode
    mode=True
    choice=1
    gameDisplay.fill(white)
    
    while mode:
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Test Your Accuracy",black,0,500,300,70,green,shade,action="Accuracy")
        button("Game Mode",black,300,500,300,70,green,shade,action="GameMode")
        button("FPP Shooter",black,600,500,300,70,green,shade,action="FPP")
        button("Training Ground",black,900,500,300,70,green,shade,action="Training")
        if mode==False:
            
            if choice==1:
                Gameloop()
            if choice==0:
                GameMode()
            if choice==2:
                GameFPP()
            if choice==3:
                GameTrain()

        pygame.display.update()
        clock.tick(25)
def button(txt,color,buttonx,buttony,buttonwidth,buttonheight,active_color,inactive_color,action):
    global start
    global setting
    global gameover
    global gameexit
    global choice
    global mode
    curser=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if (buttonx+buttonwidth>curser[0] and curser[0]>buttonx) and buttony+buttonheight>curser[1]>buttony:
        pygame.draw.rect(gameDisplay,active_color,[buttonx,buttony,buttonwidth,buttonheight])
        if click[0]==1:
            #####problem is before pressing on page may result in click on later pages
            if action=="Quit":
                pygame.quit()
                quit()
            if action=="Play":
                start=False
                #Modes()
            if action=="GameMode":
                mode=False
                choice=0
                #GameMode()
            if action=="Accuracy":
                mode=False
                choice=1
            if action=="FPP":
                mode=False
                choice=2
            if action=="Training":
                mode=False
                choice=3
                #Gameloop()
            
            #if action=="Setting":
             #   setting()
            
            if action=="Mode":
                
                gameover=False
                #gameexit=True
                #start()
    else:
        pygame.draw.rect(gameDisplay,inactive_color,[buttonx,buttony,buttonwidth,buttonheight])
    message_button(txt,color,buttonx,buttony,buttonwidth,buttonheight)

def start():
    global start
    global setting
    start=True
    gameDisplay.fill(white)
    message("Aim Trainer",blue,-170,"largefont")
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Play",black,550,200,100,50,green,white,action="Play")
        #button("Setting",black,200,380,200,50,green,white,action="Setting")
        button("Quit",black,550,300,100,50,green,white,"Quit")
        if start==False:
            Modes()
            
        pygame.display.update()
        clock.tick(30)
    
def text(txt,color,size):
    if size=="smallfont":
        textsurface=smallfont.render(txt,True,color)
    if size=="medfont":
        textsurface=medfont.render(txt,True,color)
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




def GameMode():
    global gameover
    gameover=True
    
    gameDisplay.fill(white)
    message("Under Development",blue,-170,"medfont")
    while gameover:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        button("Change Modes",black,500,200,200,50,green,shade,action="Mode")
        button("Quit",black,500,255,200,50,green,shade,"Quit")
        if gameover==False:
            Modes()
        pygame.display.update()
        clock.tick(30)

def Gameloop():
    global gameover
    gameexit= False
    gameover=False
    damage=100
    timer=0
    start_ticks=pygame.time.get_ticks()
    turn=0
    hits=0
    x=random.randint(0,display_width-3)
    y=random.randint(0,display_height-10)
    x_change=0
    count=0
    global pos
    pos=[0,0]
    
    pygame.mouse.set_visible(False)
    
    #global start
    #global setting
    while not gameexit:
        while gameover==True:#when fails
            gameDisplay.fill(white)
            pygame.mouse.set_visible(True)
            message('Accuracy:{}'.format(round(1000/hits,1)),shade,-170,'smallfont')
            message('Time Taken:{}'.format(round(timer,1)),shade,-200,'smallfont')
            message('Score: {} Out Of 100'.format(round(10000/(hits*timer),1)),shade,-140,'smallfont')
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            
            button("Change Modes",black,500,200,200,50,green,shade,action="Mode")
            button("Quit",black,500,255,200,50,green,shade,"Quit")
            pygame.display.update()
            if gameover==False:
                Modes()           


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            pos=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            #print(click)
            if click[0]==1 and turn==0:
                hits+=1
                if pos[0]<=x+5 and pos[0]>=x and pos[1]<=y+3 and pos[1]>=y:
                    damage+=101
                    turn=1
                elif pos[0]<=x+5 and pos[0]>=x and pos[1]<=y+12 and pos[1]>=y+3:
                    damage+=45
                    turn=1
                elif pos[0]<=x+7 and pos[0]>=x-2 and pos[1]<=y+14 and pos[1]>=y-2:
                    damage+=20
                    turn=1
            if click[0]==0:
                turn=0
            #click=pygame.mouse.get_pressed()
            
        gameDisplay.fill(white)

        #gameover=True
        if damage>=100:
            x=random.randint(0,display_width-3)
            y=random.randint(0,display_height-10)
            damage=0
            count+=1
            if count>=11:
                gameover=True
        
        if count>=5 and count<10:
            if count==5:
                x_change=1
            if x<7:
                x_change=2
            if x>display_width-10:
                x_change=-3
        if count==10:
            x_change=random.randint(-2,3)
            
            if x<7:
                x_change=random.randint(0,3)
            elif x>display_width-5:
                x_change=random.randint(-3,0)
        x+=x_change
        pygame.draw.rect(gameDisplay, black, [x,y,5,12])
        gameDisplay.blit(dot,[pos[0]-103,pos[1]-70])
        #background.blit(dot,[0,0])

        timer=(pygame.time.get_ticks()-start_ticks)/1000
        message('Time Elapsed',red,-280,'smallfont')
        message('{}'.format(round(timer,1)),red,-255,'smallfont')
        pygame.display.update()
        clock.tick(60)

def GameTrain():
    global gameover
    gameexit= False
    gameover=False
    damage=100
    timer=0
    start_ticks=pygame.time.get_ticks()
    turn=0
    hits=0
    x=random.randint(0,display_width-3)
    y=random.randint(0,display_height-10)
    x_change=0
    count=0
    global pos
    pos=[0,0]
    
    pygame.mouse.set_visible(False)
    message('Time Elapsed',red,-280,'smallfont')
    #global start
    #global setting
    while not gameexit:
        while gameover==True:#when fails
            gameDisplay.fill(white)
            pygame.mouse.set_visible(True)
            #message('Accuracy:{}'.format(round(1000/hits,1)),shade,-170,'smallfont')
            #message('Time Taken:{}'.format(round(timer,1)),shade,-200,'smallfont')
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            
            button("Change Modes",black,500,225,200,50,green,shade,action="Mode")
            button("Quit",black,500,325,200,50,green,shade,"Quit")
            pygame.display.update()
            if gameover==False:
                Modes()           


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            pos=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            #print(click)
            if click[0]==1 and turn==0:
                hits+=1
                if pos[0]<=x+5 and pos[0]>=x and pos[1]<=y+3 and pos[1]>=y:
                    damage+=101
                    turn=1
                elif pos[0]<=x+5 and pos[0]>=x and pos[1]<=y+12 and pos[1]>=y+3:
                    damage+=45
                    turn=1
                elif pos[0]<=x+7 and pos[0]>=x-2 and pos[1]<=y+14 and pos[1]>=y-2:
                    damage+=20
                    turn=1
            if click[0]==0:
                turn=0
            #click=pygame.mouse.get_pressed()
            
        gameDisplay.fill(white)

        gameover=True
        if damage>=100:
            x=random.randint(0,display_width-3)
            y=random.randint(0,display_height-10)
            damage=0
            count+=1
            if count>=11:
                gameover=True
        
        if count>=5 and count<10:
            if count==5:
                x_change=1
            if x<7:
                x_change=2
            if x>display_width-10:
                x_change=-3
        if count==10:
            x_change=random.randint(-2,3)
            
            if x<7:
                x_change=random.randint(0,3)
            elif x>display_width-5:
                x_change=random.randint(-3,0)
        x+=x_change
        pygame.draw.rect(gameDisplay, black, [x,y,5,12])
        gameDisplay.blit(dot,[pos[0]-103,pos[1]-70])
        #background.blit(dot,[0,0])

        timer=(pygame.time.get_ticks()-start_ticks)/1000
        message('{}'.format(timer),red,-260,'smallfont')
        pygame.display.update()
        clock.tick(60)

def GameFPP():
    global gameover
    gameexit= False
    gameover=False
    damage=100
    timer=0
    start_ticks=pygame.time.get_ticks()
    turn=0
    scope=True
    Accuracy=0
    flip=0
    x=random.randint(0,display_width-3)
    y=random.randint(0,display_height-10)
    x_back=-1400
    y_back=-600
    count=0
    global pos
    pos=[0,0]
    
    
    pygame.mouse.set_visible(False)
    
    #global start
    #global setting
    pygame.event.set_grab(True)
    while not gameexit:
        rel_pos=[0,0]

        while gameover==True:#when fails
            pygame.event.set_grab(False)
            gameDisplay.fill(white)
            pygame.mouse.set_visible(True)
            message('Accuracy:{}'.format(round(Accuracy*10,1)),shade,-170,'smallfont')
            message('Time Taken:{}'.format(round(timer,1)),shade,-200,'smallfont')
            message('Score: {} Out Of 100'.format(round(100*Accuracy/timer,1)),shade,-140,'smallfont')
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            
            button("Change Modes",black,500,225,200,50,green,shade,action="Mode")
            button("Quit",black,500,325,200,50,green,shade,"Quit")
            pygame.display.update()
            if gameover==False:
                Modes()           


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LCTRL:
                    pygame.mouse.set_visible(True)
                    pygame.event.set_grab(False)
                if event.key == pygame.K_LSHIFT:
                    pygame.mouse.set_visible(False)
                    pygame.event.set_grab(True)

            if event.type == pygame.MOUSEMOTION:
                rel_pos=(event.rel)
                #print(rel_pos)
            
            pos=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            #print(click)
            if click[0]==1 and turn==0:
                mixer.music.play() 
                
                if (600-x)**2+(300-y)**2<=49:
                    damage+=101
                    Accuracy+=abs(((600-x)**2+(300-y)**2)/49-1)
                    turn=1
                y+=3
                y_back+=3
                x+=1
                x_back+=1

            if click[2]==1 and scope:
                flip+=1
                scope=False
            if click[0]==0:
                turn=0
            if click[2]==0:
                scope=True
            #click=pygame.mouse.get_pressed()
           
        gameDisplay.fill(white)

        #gameover=True
        if damage>=100:
            x=random.randint(x_back+1400,x_back+2600)
            y=random.randint(y_back+600,y_back+1200)
            damage=0
            count+=1
            if count>=11:
                gameover=True

        if x_back<display_width/2 and x_back+3840>display_width/2 and y_back<display_height/2 and y_back+2160>display_height/2:
            ###To Not Move Outside of wallpaper(3840*2160)
            #rel_move work only inside wallpaper
            x-=rel_pos[0]
            y-=rel_pos[1]
            x_back-=rel_pos[0]
            y_back-=rel_pos[1]
        else:
            x-=(x_back+1400)
            y-=(y_back+600)
            x_back=-1400
            y_back=-600

        gameDisplay.blit(background,[x_back,y_back])
        pygame.draw.circle(gameDisplay , blue, [x,y], 7)
        
        if flip%2==0:
            gameDisplay.blit(gun,[0,0])
        elif flip%2==1:
            gameDisplay.blit(scopes,[0,0])
        
        
        timer=(pygame.time.get_ticks()-start_ticks)/1000
        message('Time Elapsed',red,-280,'smallfont')
        message('{}'.format(round(timer,1)),red,-260,'smallfont')
        pygame.display.update()
        clock.tick(60)




start()####again entering same func may result in error,use any func instead of start()
#Gameloop()
pygame.quit()
quit()