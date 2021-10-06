import pygame
pygame.init()
game_display = pygame.display.set_mode((800,600))
pygame.mouse.set_visible(False)

exit = False

while (not exit):
    
    pygame.event.set_grab(True)###grab mouse inside
    #mouse_move = (0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit = True
        if event.type == pygame.MOUSEMOTION:
            print(event.rel)###give relative mouse speed
    #if mouse_move != (0,0):
     #   print(mouse_move)

pygame.quit()
            
            
            