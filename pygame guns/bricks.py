import pygame
from pygame.locals import *
pygame.init()
import mysql
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sksjr@2000',
    database='Brick_Game'
)
mycursor=mydb.cursor()
global user
user=''
#from pygame import mixer 
import time
# Starting the mixer
#mixer.init()
clock=pygame.time.Clock()
# Loading the song
#mixer.music.load(r"C:\Users\saurabh\Documents\Desktop\pygame guns\supp_m16.mp3")
white=(225,225,225)
black=(0,0,0)
red=(225,0,0)
green=(10,160,5)
shade=(255,30,255)
blue=(0,0,100)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('break game')
block=5
smallfont=pygame.font.SysFont('Segoe Print',28)
medfont=pygame.font.SysFont('Segoe Print',36)
largefont=pygame.font.SysFont('Segoe Print',64)
block_size=20
global level
level=1
global total_score
total_score=0


def helps():
    global helpss
    helpss=True
    mycursor.execute('select * from score order by scores desc')

    print(mycursor.fetchall()[0])
    mycursor.execute("select * from score  where username='{}' order by scores desc".format(user))
    print(mycursor.fetchall()[0])
        



    gameDisplay.fill(white)
    while helpss:
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button('<-',black,100,100,50,50,blue,shade,'back')
        if helpss==False:
            Modes()
        pygame.display.update()
        clock.tick(7)

def SQLs():
    global sql 
    sql=True
    global user
    global pin 
    user=''
    name=''
    pin=-1
    while sql:
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key==K_0:
                    name+=chr(event.key)
                elif event.key==K_1:
                    name+=chr(event.key)
                elif event.key==K_2:
                    name+=chr(event.key)
                elif event.key==K_3:
                    name+=chr(event.key)
                elif event.key==K_4:
                    name+=chr(event.key)
                elif event.key==K_5:
                    name+=chr(event.key)
                elif event.key==K_6:
                    name+=chr(event.key)
                elif event.key==K_7:
                    name+=chr(event.key)
                elif event.key==K_8:
                    name+=chr(event.key)
                elif event.key==K_9:
                    name+=chr(event.key)

                elif event.key == K_RETURN:
                    if len(user)==0:
                        user=(name)
                        
                            


                    elif len(user)!=0 and pin==-1:
                        try:
                            pin=int(name)
                            mycursor.execute("select username from users where username='{}'".format(str(user)))
                            if len(mycursor.fetchall())!=0:
                                mycursor.execute("select pin from users where username='{}'".format(str(user)))
                                if pin!=mycursor.fetchall()[0][0]:
                                    pin=-1
                                    user=''
                                    #message('Wrong PIN!!!',red,0)
                                    



                        except ValueError:
                            pass
                                #message('Enter 4 DIGIT PIN!!!',red,0)

        
                   

                    name = ""
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                

        gameDisplay.fill(white)
        message('Log In',blue,-200)
        if len(user)==0:
            message('Enter Username',red,0)
            message('Press Enter!!!',blue,-100)
        elif len(user)!=0:
            message('Enter 4 digit PIN',black,0)
            message('Press Enter!!!',black,-100)
        message(name,blue,100)
        button('<-',black,100,100,50,50,blue,shade,'back')
        if pin!=-1:
            button('Save',black,display_width//2,display_height-250,100,50,blue,shade,'save')
        

        if sql==False:
            pin=-1
            user=''
            Modes()
        if sql=='saved':
            Modes()
        pygame.display.update()
        clock.tick(7)





def settings():
    global setting
    setting=True
    gameDisplay.fill(white)
    while setting:
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button('<-',black,100,100,50,50,blue,shade,'back')
        if setting==False:
            Modes()
        pygame.display.update()
        clock.tick(7)
def Modes():
    global choice
    global mode
    mode=True
    choice=0
    gameDisplay.fill(white)
    message('Welcome To Block Breaker',black,-150,'smallfont')
    message('Log In to Save Profile And High Scores',black,-110,'smallfont')
    while mode:
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Start Game",black,0,500,200,70,green,shade,action="Game")
        button("Settings",black,200,500,200,70,green,shade,action="setting")
        if len(user)==0:
            button('Log In',black,400,500,200,70,green,shade,action="Logs")
        else:
            button(user,black,400,500,200,70,green,shade,action="Logs")
        button('LeaderBoard',black,600,500,200,70,green,shade,action="help")
        button('',black,700,100,50,50,green,shade,action="mute")
        
        if mode==False:
            
            if choice==1:
                settings()
            elif choice==0:
                Gameloop()

            elif choice==2 and len(user)==0:
                SQLs()
            elif choice==2 and len(user)!=0:
                mode=True
            elif choice==3 and len(user)!=0:
                helps()
            elif choice==3 and len(user)==0:
                mode=True

        pygame.display.update()
        clock.tick(25)

def button(txt,color,buttonx,buttony,buttonwidth,buttonheight,active_color,inactive_color,action):
    global start
    global setting
    global gameover
    global gameexit
    global choice
    global mode
    global level
    global sql
    global helpss
    global user
    global pin

    curser=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if (buttonx+buttonwidth>curser[0] and curser[0]>buttonx) and buttony+buttonheight>curser[1]>buttony:
        pygame.draw.rect(gameDisplay,active_color,[buttonx,buttony,buttonwidth,buttonheight])
        if click[0]==1:
            #####problem is before pressing on page may result in click on later pages
            if action=="Quit":
                pygame.quit()
                quit()
            elif action=="Play":
                start=False
            elif action=='Game':
                mode=False
                choice=0
            elif action=='setting':
                choice=1
                mode=False
            elif action=='Logs':
                choice=2
                mode=False
            elif action=='help':
                choice=3
                mode=False
            elif action=='mute':
                pass
            elif action=='levels':
                level+=1
                gameover=False
                Gameloop()
            elif action=="Mode":
                Modes()
            elif action=="back":
                helpss=False
                setting=False
                sql=False
                #user=''
                #pin=-1
                gameexit=True
            elif action=="save":
                ###Queries
                mycursor.execute("select username from users where username='{}'".format(str(user)))
                if len(mycursor.fetchall())==0:
                    mycursor.execute("insert into users values('{}',{})".format(str(user),int(pin)))
                    mydb.commit()
                print(user,'****')
                sql='saved'
            
                
                
    else:
        pygame.draw.rect(gameDisplay,inactive_color,[buttonx,buttony,buttonwidth,buttonheight])
    message_button(txt,color,buttonx,buttony,buttonwidth,buttonheight)

def start():
    global start
    start=True
    gameDisplay.fill(white)
    message("BRICK BREAKER",blue,-170,"largefont")
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Start->",black,550,200,100,50,green,white,action="Play")
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


def Gameloop():
    global gameover
    global gameexit
    global total_score
    gameexit= False
    gameover=False
    turn=0
    Arr2=[]
    for a in range(0,display_height//2,2*block_size):
        if a%(4*block_size)==0:
            for b in range(0,display_width,6*block_size):
                Arr2.append([b,a])
        else:
            for c in range(3*block_size,display_width,6*block_size):
                Arr2.append([c,a])


    Arr3=[]
    for a in range(0,display_height//5,block_size+5):
        for b in range(0,display_width,2*block_size+5):
            Arr3.append([b,a])
    for a in range(display_height//5+5,display_height//3,block_size+5):
        for b in range(0,display_width//4,2*block_size+5):
            Arr3.append([b,a])
        for c in range((3*display_width)//4,display_width,2*block_size+5):
            Arr3.append([c,a])
    for a in range(display_height//3+5,display_height//3+25,block_size+5):
        for b in range(0,display_width,2*block_size+5):
            Arr3.append([b,a])


    Arr1=[[a,b] for a in range(0,display_width,2*block_size+5) for b in range(0,80,block_size+5)]
    Arr=[Arr1,Arr3,Arr2]
    x=display_width//2+3*block_size-10
    y=540
    #this makes less change if we change the resolution of the display
    x_change=0
    y_change=0
    x_break=display_width//2
    y_break=550
    x_breakchange=0
    
    score=0
    clock=pygame.time.Clock()
    while not gameexit:

        while gameover==True:
            gameDisplay.fill(white)
            if turn==0:
                message('You Failed, Score:{}'.format(score),shade,-140,'smallfont')


            elif turn==2:
                message('Game Completed, Score:{}'.format(score),shade,-140,'smallfont')


            else:
                message('Level {} Completed'.format(level),shade,-140,'smallfont')
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            if turn!=0 and  turn!=2:
                button("Next Level->",black,0,100,200,50,green,shade,action="levels")
            else:
                button("Main Menu->",black,0,250,200,50,green,shade,action="Mode")
                button("Quit->",black,0,400,200,50,green,shade,"Quit")
            pygame.display.update()

            #if gameover==False:
             #   Modes()          

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_breakchange=-2*block
                    if event.key==pygame.K_RIGHT:
                        x_breakchange=2*block
                    if event.key==pygame.K_UP:
                        if turn==0:
                            turn=1
                            y_change=-block
                            x_change=block

            if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        x_breakchange=0
                    if event.key==pygame.K_RIGHT:
                        x_breakchange=0


        for coords in Arr[level-1]:
            x1=coords[0]
            x2=coords[0]+block_size*2-1
            y1=coords[1]
            y2=coords[1]+block_size-1
            if (100-(y2-y)**2)>=0:
                if (100-(x1-x)**2)>=0 or (100-(x2-x)**2)>=0:
                    y_change=block
                    Arr[level-1].remove(coords)
                    score+=1
                elif x1<=x and x2>=x:
                    y_change=block
                    Arr[level-1].remove(coords)
                    score+=1
            elif (100-(x1-x)**2)>=0:###x line cuts
                if (100-(y1-y)**2)>=0 or (100-(y2-y)**2)>=0: ###y line also cuts
                    x_change=-block
                    Arr[level-1].remove(coords)
                    score+=1
                elif y1<=y and y2>=y:###if y line not cut may be circle is smaller
                    x_change=-block
                    Arr[level-1].remove(coords)
                    score+=1
            
            elif (100-(x2-x)**2)>=0:
                if (100-(y1-y)**2)>=0 or (100-(y2-y)**2)>=0:
                    x_change=block
                    Arr[level-1].remove(coords)
                    score+=1
                elif y1<=y and y2>=y:
                    x_change=-block
                    Arr[level-1].remove(coords)
                    score+=1
            
            elif (100-(y1-y)**2)>=0:
                if (100-(x1-x)**2)>=0 or (100-(x2-x)**2)>=0:
                    y_change=-block
                    Arr[level-1].remove(coords)
                    score+=1
                elif x1<=x and x2>=x:
                    y_change=-block
                    Arr[level-1].remove(coords)
                    score+=1
            elif (100-(y2-y)**2)>=0:
                if (100-(x1-x)**2)>=0 or (100-(x2-x)**2)>=0:
                    y_change=block
                    Arr[level-1].remove(coords)
                    score+=1
                elif x1<=x and x2>=x:
                    y_change=block
                    Arr[level-1].remove(coords)
                    score+=1


        if y>=540 and y<=544:
            if x_break<=x and x_break+6*block_size>=x:
                y_change=-block
                x_change+=x_breakchange//2##friction
            elif ((x_break-x)<10 and (x_break-x)>0)  or ((x-(x_break+6*block_size))<10 and (x-(x_break+6*block_size))>0):
                y_change=-block   ###edge
                x_change=-x_change


        if x<=10:
            x_change=block
        if x>=display_width-10:
            x_change=-block
        if y<=10:
            y_change=block
        if y>=display_height:
            gameover=True
            turn=0
            total_score+=score
            mycursor.execute("insert into score values('{}',{})".format(str(user),int(total_score)))
            mydb.commit()
            total_score=0


        if turn==0:
            x=x_break+3*block_size
            y=540
            x_change=0
            y_change=0
        
            
        ####ADdd MORE CASES FOR NEW DESIGN
        
        
        x+=x_change
        y+=y_change
        

        if x_break<0:
            x_break=0
            x_breakchange=0
        if x_break>(display_width-6*block_size):
            x_break=(display_width-6*block_size)
            x_breakchange=0

        
        
            
        




            




        
        x_break+=x_breakchange
        gameDisplay.fill(white)

        
        for xb,yb in Arr[level-1]:
            pygame.draw.rect(gameDisplay, blue, [xb,yb,2*block_size-1,block_size-1])


        message('Score:{}'.format(score),black,280,'smallfont')
        pygame.draw.circle(gameDisplay, black, [x,y], 10)
        #pygame.draw.rect(gameDisplay, black, [x,y,block_size,block_size])
        pygame.draw.rect(gameDisplay, red, [x_break,y_break,6*block_size,block_size//3])
        pygame.draw.line(gameDisplay, black, (0,550),(display_width,550),1)

        if len(Arr[level-1])==0 and level<=len(Arr):
            gameover=True
            total_score+=score
            
        elif len(Arr[level-1])==0 and level>len(Arr):
            turn=2
            gameover=True
            total_score+=score
            mycursor.execute("insert into score values('{}',{})".format(str(user),int(total_score)))
            mydb.commit()
            total_score=0
        button('<-',black,0,550,50,50,blue,shade,'back')
        if gameexit==True:
            Modes()
        pygame.display.update()
        clock.tick(70)
start()
pygame.quit()
mydb.close()
quit()


