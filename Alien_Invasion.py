import sys
import pygame
from settings import Settings
from pygame.constants import QUIT

def run_game():
    #Initializing the game window and setting the caption
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #setting the background color of the screen
    bg_color = (230, 230, 230)
    #Running the game main loop
    while True:
        #Evaluating Events by mouse and keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redrawing the color every loop
        screen.fill(ai_settings.bg_color)
        #Making the last drawn screen visible
        pygame.display.flip()

run_game()
