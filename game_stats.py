class Game_stats():
    """Track the statistics of the game"""
    def __init__(self, ai_settings):
        """Start Statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
    
    def reset_stats(self):
        """Start changing statistics"""
        self.ships_left = self.ai_settings.ship_limit