import sys
import pygame
from pygame.constants import K_DOWN, K_UP

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                ship.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                ship.rect.centerx -= 1
            elif event.key == pygame.K_UP:
                ship.moving_up = True
                ship.rect.bottom -= 1
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
                ship.rect.bottom += 1
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    #Redrawing the color every loop
    screen.fill(ai_settings.bg_color)
    #Drawing the ship
    ship.blitme()
    #Making the last drawn screen visible
    pygame.display.flip()
