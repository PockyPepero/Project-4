class Settings:
    """A class to store the settings for Exercise 13.3-4."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Raindrop settings
        self.raindrop_speed = 1.0