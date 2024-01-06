import pygame
from pygame.constants import QUIT

pygame.init()
FPS = pygame.time.Clock()

HEIGT = 800
WIDTH = 1200
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
NEW_COLOR = (0, 255, 0)
NEW_COLOR_TWO = (125, 0, 125)

main_display = pygame.display.set_mode((WIDTH, HEIGT)) # задаємо розміри екрану

player_sixe = (20, 20)

player = pygame.Surface(player_sixe)
player.fill(COLOR_WHITE)

player_rect = player.get_rect()
player_speed = [1, 1]
playing = True

while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    if  player_rect.top < 0 or player_rect.bottom >= HEIGT:
        player_speed[1] = -player_speed[1]
        
    if player_rect.right >= WIDTH or player_rect.left < 0:
        player_speed[0] = -player_speed[0]
           
    main_display.blit(player, player_rect)  
    player_rect = player_rect.move(player_speed)   
    pygame.display.flip()   