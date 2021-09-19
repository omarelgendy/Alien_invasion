import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initializing the game window and setting the caption
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    #Running the game main loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
<<<<<<< Updated upstream
=======
        
>>>>>>> Stashed changes

run_game()
