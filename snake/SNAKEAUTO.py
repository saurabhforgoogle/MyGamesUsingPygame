#updates like not moving in opposite to the direction it is moving
#bug like not error while touching end boundaries
#changing the style codes
import pygame
import random
import time
pygame.init()
white=(225,225,225,0.8)
black=(0,0,0)
red=(225,0,0)
green=(10,160,5,0.9)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('game')
block=20
block_size=20
applesize=30
#for different size of snake and apple,if slight contact,it ate apple
#remove rounnding,change sizes



font=pygame.font.SysFont(None,25)
def snake(block_size,snakelist):
    for xny in snakelist:
        pygame.draw.rect(gameDisplay, green, [xny[0],xny[1],block_size,block_size])
def Gameloop():
    gameexit= False
    x=display_width/2
    y=display_height/2 #this makes less change if we change the resolution of the display
    x_change=0
    y_change=0
    a=b=c=d=1
    snakelist=[]
    snakelength=1
    randx=random.randrange(0,display_width-applesize)
    randy=random.randrange(0,display_height-applesize)
    clock=pygame.time.Clock()
    while not gameexit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
                
        if True:#rules
            if x>(randx+applesize) and x_change==0 and a!=0:
                    x_change=-block
                    y_change=0
            elif a==0 and y-randy>0:#rules in prevention of crash
                y_change=-block
                x_change=0
            elif a==0 and y-randy<0:
                y_change=block
                x_change=0

            if x<(randx-block_size) and x_change==0 and c!=0:
                    x_change=block
                    y_change=0
            elif c==0 and y-randy>0:
                y_change=-block
                x_change=0
            elif a==0 and y-randy>0:
                y_change=block
                x_change=0

            if y>(randy+applesize) and y_change==0 and b!=0:
                    y_change=-block
                    x_change=0
            elif b==0 and x-randx>0:
                x_change=-block
                y_change=0
            elif b==0 and x-randx>0:
                x_change=block
                y_change=0

            if y<(randy-block_size) and y_change==0 and d!=0:
                    y_change=block
                    x_change=0 
            elif d==0 and x-randx>0:
                x_change=-block
                y_change=0
            elif b==0 and x-randx>0:
                x_change=block
                y_change=0   
        
        if x<0:
            x=display_width
        elif x>=display_width:
            x=0
        elif y<0:
            y=display_height
        elif y>=display_height:
            y=0
        a=b=c=d=1
        #check if gonna crash
        for xny in snakelist[:-1]:
            if (x-xny[0])==block_size and (y-xny[1])==0:
                a=0
            if (x-xny[0])==0 and (y-xny[1])==block_size:
                b=0
            if (x-xny[0])==-block_size and (y-xny[1])==0:
                c=0
            if (x-xny[0])==0 and (y-xny[1])==-block_size:
                d=0
            
        

        x+=x_change
        y+=y_change
        gameDisplay.fill(white)  
        
        pygame.draw.rect(gameDisplay, red, [randx,randy,applesize,applesize])
        snakehead=[]
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]
        for coordinates in snakelist[0:snakelength-1:1]:
            if coordinates==snakehead and snakelength>=3:
                gameexit=True
        snake(block_size,snakelist)
        pygame.display.update()
        if x>=(randx-block_size) and x<=(randx+applesize) and y>=(randy-block_size) and y<=(randy+applesize):
            randx=random.randrange(0,display_width-block_size)
            randy=random.randrange(0,display_height-block_size) 
            snakelength+=1

        clock.tick(30)
Gameloop()
pygame.quit()
quit()