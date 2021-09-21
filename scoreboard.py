import pygame.font

class Scoreboard():
    """A class to report score information"""
    def __init__(self, ai_settings, screen, stats):
        """Set scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (243, 189, 34)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_highscore()

    def prep_score(self):
        """Turn the score to a rendered image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highscore(self):
        """Turn highscore into a rendered image"""
        highscore = int(round(self.stats.highscore, -1))
        highscore_str = "{:,}".format(highscore)
        self.highscore_image = self.font.render(highscore_str, True, self.text_color, self.ai_settings.bg_color)
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.screen_rect.top


    
    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)