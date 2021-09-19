import sys
import pygame
from bullet import Bullet
        
def check_keydown_events(event, ai_settings, screen, ship, bullets):
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
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    #Redrawing the color every loop
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #Drawing the ship
    ship.blitme()
    #Making the last drawn screen visible
    pygame.display.flip()
