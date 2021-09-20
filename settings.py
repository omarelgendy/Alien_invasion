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
        self.bullet_width = 5
        self.bullet_speed_factor = 1
        self.bullet_color = (243, 189, 34)
        self.bullets_allowed = 5

        self.alien_speed_factor = 0.7
        self.fleet_drop_speed = 6
        self.fleet_direction = 1

        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.dynamic_settings()

    def dynamic_settings(self):
        """Start settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale