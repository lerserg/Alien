class Settings:
    """Class for game settings storage"""

    def __init__(self) -> None:
        """Initializes static game settings"""
        #resourses
        self.ship_img = 'images/ship.bmp'
        self.alien_img = 'images/alien.bmp'
        #screen
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (25, 25, 112)
        #ship
        self.ship_limit = 3
        #bullets
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3
        #aliens
        self.alien_speed = 0.7
        self.alien_drop_speed = 10
        self.alien_direction = -1
        #game temp
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1
        self.bullet_speed = 3
        self.alien_speed = 0.7
        self.alien_direction = -1
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale