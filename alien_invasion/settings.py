class Settings:
    """A class to store the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 209, 220)

        # Ship settings
        self.ship_speed = 1.5