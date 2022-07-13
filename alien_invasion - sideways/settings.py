class Settings:
    """A class to store the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 209, 220)
        self.bullets_allowed = 10

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 105, 180)

        # Alien settings
        self.alien_speed = 0.3
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents down, -1 is up
        self.fleet_direction = 1
