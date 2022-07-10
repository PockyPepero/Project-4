import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a raindrop in the storm."""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop at the top left corner of the screen.
        self.rect.x  = self.rect.width 
        self.rect.y = self.rect.height

        # Store the raindrop's exact positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """
        Return True if the bottom row of raindrops 
        is at the bottom of the screen.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True







