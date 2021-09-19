class Settings():
    """A class to store all settings to alien invasion game"""
    def __init__(self):
        """Initialize the game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 0.7

        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_speed_factor = 0.4
        self.bullet_color = (60, 60, 60)
