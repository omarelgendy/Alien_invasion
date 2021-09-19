class Settings():
    """A class to store all settings to alien invasion game"""
    def __init__(self):
        """Initialize the game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 1, 23)
        self.ship_speed_factor = 1.5

        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_speed_factor = 1
        self.bullet_color = (243, 189, 34)
        self.bullets_allowed = 10

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1