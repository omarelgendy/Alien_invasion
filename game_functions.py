import sys
import pygame
from bullet import Bullet
from alien import Alien
        
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
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()

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

def create_fleet(ai_settings, screen, aliens):
    """Create a fleet of the ALiens"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 1.5 * alien_width
    number_aliens_x = int(available_space_x / (1.5 * alien_width))
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 1.5 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

def update_bullets(bullets):
    """Update the position of the bullets and get rid of old ones"""
    bullets.update()

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    #Redrawing the color every loop
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #Drawing the ship
    ship.blitme()
    #Drawing the alien
    aliens.draw(screen)
    #Making the last drawn screen visible
    pygame.display.flip()
