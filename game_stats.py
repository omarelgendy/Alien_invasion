class Game_stats():
    """Track the statistics of the game"""
    def __init__(self, ai_settings):
        """Start Statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
    
    def reset_stats(self):
        """Start changing statistics"""
        self.ships_left = self.ai_settings.ship_limit