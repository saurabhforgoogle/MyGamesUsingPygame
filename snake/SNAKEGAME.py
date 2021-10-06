#updates like not moving in opposite to the direction it is moving
#bug like not error while touching end boundaries
#changing the style codes
import pygame
import random
import time
pygame.init()
white=(225,225,225)
black=(0,0,0)
red=(225,0,0,0.4)
green=(10,160,5)
blue=(0,0,100)
lightgreen=(0,255,127,0.5)
lightgrey=(60,179,113,0.4)
lightblue=(152,251,152,0.3)
#eatsound=pygame.mixer.Sound("eatapple.wav")
global direction
icon=pygame.image.load(r'C:\Users\saurabh\Documents\Desktop\Projects\pygame\snake\apple2.png')
head=pygame.image.load(r'C:\Users\saurabh\Documents\Desktop\Projects\pygame\snake\snakehead.png')
#tail=pygame.image.load('snaketail.png')
snake1=pygame.image.load(r'C:\Users\saurabh\Documents\Desktop\Projects\pygame\snake\snake.png')
pygame.display.set_icon(icon)
smallfont=pygame.font.SysFont('Segoe Print',28)
medfont=pygame.font.SysFont('Segoe Print',36)
largefont=pygame.font.SysFont('Segoe Print',64)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('game')
block=20
block_size=20
applesize=30
global start
global setting
p=2
clock=pygame.time.Clock()

#for different size of snake and apple,if slight contact,it ate apple
#remove rounnding,change sizes
font=pygame.font.SysFont(None,25)
def setting():
    global setting
    global start
    setting=True
    gameDisplay.fill(white)
    message(">>>Change Level:",blue,-240,"medfont")
    #message("Press 2: Level 2",blue,10,"medfont")
    #message("Press 3:Level 3",blue,60,"medfont")
    message("Rules: Eat  apples without touching the corner",black,190)
    message("Don't touch part of snake",black,240)
    while setting:
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button(">Level 1",black,100,150,150,50,red,blue,"save1")
        button(">Level 2",black,325,150,150,50,red,blue,"save2")
        button(">Level 3",black,550,150,150,50,red,blue,"save3")
        #button("Go Back",black,300,360,200,70,red,blue,"back")
        
        pygame.display.update()
        #if setting==False:
            #return p
            
            #start()
            #Gameloop()
        clock.tick(7)
        


def button(txt,color,buttonx,buttony,buttonwidth,buttonheight,active_color,inactive_color,action):
    global paused
    global start
    global p
    global setting
    global gameover
    global gameexit

    curser=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if (buttonx+buttonwidth>curser[0] and curser[0]>buttonx) and buttony+buttonheight>curser[1]>buttony:
        pygame.draw.rect(gameDisplay,active_color,[buttonx,buttony,buttonwidth,buttonheight])
        if click[0]==1:
            if action=="Continue":
                paused=False
            if action=="Quit":
                pygame.quit()
                quit()
            if action=="Play":
                print("fg")
                start=False
            if action=="Playagain":
                Gameloop()
            if action=="Setting":
                setting()
            if action=="back":
                pass
                #starts()
                #Gameloop()
                
                
            if action=="save1":
                p=2
                message("setting succesfully changed",red,0,"medfont")
                setting=False
                starts()
                Gameloop()
            if action=="save2":
                p=3
                message("setting succesfully changed",red,0,"medfont")
                setting=False
                starts()
                Gameloop()
            if action=="save3":
                p=4
                message("setting succesfully changed",red,0,"medfont")
                setting=False
                starts()
                Gameloop()
            if action=="start":
                gameover=False
                gameexit=False
                starts1()
                Gameloop()

    else:
        pygame.draw.rect(gameDisplay,inactive_color,[buttonx,buttony,buttonwidth,buttonheight])
    message_button(txt,color,buttonx,buttony,buttonwidth,buttonheight)


def textbutton(txt,color,buttonx,buttony,buttonwidth,buttonheight,active_color,action):
    curser=pygame.mouse.get_pos()
    global p
    global paused
    click=pygame.mouse.get_pressed()
    if (buttonx+buttonwidth>curser[0] and curser[0]>buttonx) and buttony+buttonheight>curser[1]>buttony:
        pygame.draw.rect(gameDisplay,active_color,[buttonx,buttony,buttonwidth,buttonheight])
        if click[0]==1:
            if action=="1":
                p=2
                paused=False
            elif action=="2":
                p=3
                paused=False
            elif action=="3":
                p=4
                paused=False
            elif action=="Pause":
                pause()
            

    message_button(txt,color,buttonx,buttony,buttonwidth,buttonheight)
    




def design():
    m=n=-20
    #creating every small block 40*30 matrix,and adding different colour alternate using even/odd.
    for i in range(30):
        n+=20
        m=-20
        for j in range(40):
            m+=20
            if ((m+n)/20)%2==0:
                pygame.draw.rect(gameDisplay,lightgrey,[m,n,20,20])
            else:
                pygame.draw.rect(gameDisplay,lightblue,[m,n,20,20])

def pause():
    global p
    global paused
    paused=True
    message("Paused",black,-150,"largefont")
    message(">>Change level :",blue,-268)
    while(paused):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            #gameDisplay.fill(white)
            #message("Press C: continue",blue,-30,"medfont")
        button("Continue",black,300,250,200,70,red,blue,"Continue")
        #message("Press q:Quit",blue,150)
        textbutton("1",blue,530,10,70,50,red,action="1")
        textbutton("2",blue,620,10,70,50,red,"2")
        textbutton("3",blue,710,10,70,50,red,"3")
        button("Quit",black,350,350,100,70,red,blue,"Quit")
        pygame.display.update()
        if paused==False:
            message("starting in 3 sec...",red,200)
            pygame.display.update()
            time.sleep(3)
            return p
        
        clock.tick(6)
                
                

def score(scor):
    text=smallfont.render("Score: "+str(scor),True,black)
    gameDisplay.blit(text,[10,0])


def start():
    
    global p
    global start
    global setting
    start=True
    gameDisplay.fill(white)
    gameDisplay.blit(snake1,(0,0))
    message("Snake Game",green,-170,"largefont")
    #gameDisplay.blit(snake,(0,0))
    
    #gameDisplay.blit(snake,(100,100))
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        button("Play",black,350,300,100,50,green,lightgreen,action="Play")
        button("Setting",black,300,380,200,50,green,lightgreen,action="Setting")
        button("Quit",black,350,460,100,50,green,lightgreen,"Quit")
        #message("Press 1: Level 1",blue,-40,"medfont")
        #message("Press 2: Level 2",blue,10,"medfont")
        #message("Press 3:Level 3",blue,60,"medfont")
        #message("Rules: Eat  apples without touching the corner",black,190)
        #message("Don't touch part of snake",black,240)
        pygame.display.update()
        clock.tick(7)
        if start==False:
            return p













def starts():
    
    global p
    global start
    global setting
    start=True
    gameDisplay.fill(white)
    message("Snake Game",green,-170,"largefont")
    #gameDisplay.blit(snake,(0,0))
    
    #gameDisplay.blit(snake,(100,100))
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        button("Play",black,350,300,100,50,green,lightgreen,action="Play")
        button("Setting",black,300,380,200,50,green,lightgreen,action="Setting")
        button("Quit",black,350,460,100,50,green,lightgreen,"Quit")
        #message("Press 1: Level 1",blue,-40,"medfont")
        #message("Press 2: Level 2",blue,10,"medfont")
        #message("Press 3:Level 3",blue,60,"medfont")
        #message("Rules: Eat  apples without touching the corner",black,190)
        #message("Don't touch part of snake",black,240)
        pygame.display.update()
        clock.tick(7)
        if start==False:
            return p
                


def snake(block_size,snakelist,direction):
    if direction=='right':
        headupdate=pygame.transform.rotate(head,270)
        #bodyupdate=pygame.transform.rotate(body,270)
        #tailupdate=pygame.transform.rotate(tail,90)
    elif direction=='left':
        headupdate=pygame.transform.rotate(head,90)
        #bodyupdate=pygame.transform.rotate(body,90)
        #tailupdate=pygame.transform.rotate(tail,270)
    elif direction=='up':
        headupdate=pygame.transform.rotate(head,0)
        #bodyupdate=pygame.transform.rotate(body,0)
        #tailupdate=pygame.transform.rotate(tail,180)
    elif direction=='down':
        headupdate=pygame.transform.rotate(head,180)
        #bodyupdate=pygame.transform.rotate(body,180)
        #tailupdate=pygame.transform.rotate(tail,0)
    #gameDisplay.blit(snake,(0,0))
    gameDisplay.blit(headupdate,(snakelist[-1][0],snakelist[-1][1]))
    #if snakelength>1:
        #gameDisplay.blit(tailupdate,(snakelist[0][0],snakelist[0][1]))
    for xny in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [xny[0],xny[1],block_size,block_size])
        #gameDisplay.blit(bodyupdate,(xny[0],xny[1]))


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




def Gameloop():
    gameexit= False
    gameover=False
    direction='right'
    x=display_width/2
    y=display_height/2 #this makes less change if we change the resolution of the display
    x_change=0
    y_change=0
    global snakelength
    global m
    global n
    global paused
    global start
    paused=False
    snakelist=[]
    snakelength=1
    global setting
    
    randx=random.randrange(0,display_width-applesize)
    randy=random.randrange(150,display_height-applesize)
    
    while not gameexit:
        if gameover==True:
            message("Game Over",red,-80,'largefont')
            #message("Press P:  Play Again",black)
            #message("Press Q:  Quit",black,70)
            #message("Press S:  Go to start",black,150)
            
            

        while gameover==True:
            #gameDisplay.fill(white)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                
            button("Play",black,350,300,100,50,green,lightgreen,action="Playagain")
            button("Quit",black,350,380,100,50,green,lightgreen,"Quit")
            #button("Main Menu",black,300,460,200,50,green,lightgreen,"start")
            pygame.display.update()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:#(moving if keydown)
                #if snake is moving in opposite to the key direction it will not work
                #if snake not moving in opposite to direction,component in that direction will be zero.
                #if event.key==pygame.K_w:
                    #pause()
                
                if event.key==pygame.K_LEFT and x_change==0:
                    x_change=-block
                    y_change=0
                    direction='left'
                elif event.key==pygame.K_RIGHT and x_change==0:
                    x_change=block
                    y_change=0
                    direction='right'
                elif event.key==pygame.K_UP and y_change==0:
                    y_change=-block
                    x_change=0
                    direction='up'
                elif event.key==pygame.K_DOWN and y_change==0:
                    y_change=block
                    x_change=0    #changing other direction value to zero if other direction key pressed
                    direction='down'
        if x>display_width-block_size or x<0 or y>display_height-block_size or y<0:
            gameover=True

        x+=x_change
        y+=y_change
        gameDisplay.fill(lightgreen) 
        if gameover==False:
            design()
    

        gameDisplay.blit(icon,[randx,randy])
        #pygame.draw.rect(gameDisplay, red, [randx,randy,applesize,applesize])
        snakehead=[]
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]
        for coordinates in snakelist[0:snakelength-1:1]:
            if coordinates==snakehead and snakelength>=3:
                gameover=True

        snake(block_size,snakelist,direction)
        score((snakelength-1)*(p-1))
        if gameover==False and paused!=True:
            textbutton("Pause",black,150,0,100,50,white,"Pause")
        pygame.display.update()
        if x>=(randx-block_size) and x<=(randx+applesize) and y>=(randy-block_size) and y<=(randy+applesize):
            randx=random.randrange(0,display_width-applesize)
            randy=random.randrange(150,display_height-applesize) 
            snakelength+=1
            #pygame.mixer.Sound.play(eatsound)
        
        
        clock.tick(7*p)
start()
Gameloop()
pygame.quit()
quit()






