import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A Class to represent a single alien in the fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and and set its initial position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    def blitme(self):
        """Draw the alien"""
        self.screen.blit(self.image, self.rect)