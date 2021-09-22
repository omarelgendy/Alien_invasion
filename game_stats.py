class Game_stats():
    """Track the statistics of the game"""
    def __init__(self, ai_settings):
        """Start Statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.highscore = 0
        self.level = 1
    
    def reset_stats(self):
        """Start changing statistics"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        #sb.show_score()