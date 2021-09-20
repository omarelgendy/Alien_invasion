import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initialize button class"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (230, 230, 230)
        self.text_color = (0, 1, 23)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_message(msg)

    def prep_message(self, msg):
        """Turn message into image"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank butten and message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
