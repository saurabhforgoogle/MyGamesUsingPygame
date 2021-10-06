

import pygame
from pygame.locals import *

def name():
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    name = ""
    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                    
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    name = ""
            elif evt.type == QUIT:
                print(name)
                return
        screen.fill((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()

if __name__ == "__main__":
    name()
    pygame.quit()


'''
import pygame
pygame.init()


def text1(word,x,y):
    font = pygame.font.SysFont(None, 25)
    text = font.render("{}".format(word), True)
    return screen.blit(text,(x,y))

def inpt():
    word=""
    text1("Please enter your name: ",300,400) #example asking name
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    word+=str(chr(event.key))
                if event.key == pygame.K_b:
                    word+=chr(event.key)
                if event.key == pygame.K_c:
                    word+=chr(event.key)
                if event.key == pygame.K_d:
                    word+=chr(event.key)
                if event.key == pygame.K_RETURN:
                    done=False
                #events...
    return text1(word,700,30)

def game_intro():
    intro=True

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    intro=False
        inpt() #Here we are calling our function
        screen.fill(white)

        pygame.display.update()
        clock.tick(15)
game_intro()

'''


