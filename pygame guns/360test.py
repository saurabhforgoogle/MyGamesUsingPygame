import pygame
import sys
import os
import math


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1000, 500])

    # player = pygame.image.load(os.path.join('img', 'rect.png')).convert_alpha() #path to cube ./img/rect.png
    player = pygame.Surface((50, 30), pygame.SRCALPHA)
    pygame.draw.polygon(player, (100, 200, 255), [(0, 0), (50, 15), (0, 30)])
    player_rect = player.get_rect(center=(500, 250)) # player rect (for center position)

    font = pygame.font.get_default_font()
    font_angle = pygame.font.SysFont(font, 44, True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        screen.fill((255, 255, 255))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dist_x = mouse_x - player_rect.centerx
        dist_y = mouse_y - player_rect.centery
        angle = -math.degrees(math.atan2(dist_y, dist_x))

        newplayer = pygame.transform.rotate(player, angle)
        # Create a new rect and pass the center of the old rect.
        player_rect = newplayer.get_rect(center=player_rect.center)

        screen.blit(newplayer, player_rect) # Blit it at the player_rect.
        text = font_angle.render(str("%.2f" % angle), 1, (255, 0, 0))
        screen.blit(text, ((mouse_x+20), mouse_y))
        pygame.display.update()

main()