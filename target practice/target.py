import pygame
from pygame.sprite import Sprite
from settings import Settings

class Target(Sprite):
    """A class to represent a single target."""

    def __init__(self, ai_game):
        """Initialize the target attributes"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Set the dimensions of the target.
        self.width, self.height = 50,100
        self.target_color = (137, 207, 240)

        # Build the target's rect object and place it at the top right
        # of the screen.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        # Store the target's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.x) 

    def draw_target(self):
        """Draw the bullet."""
        pygame.draw.rect(self.screen, self.target_color, self.rect)

    def update(self):
        """Move the target up or down."""
        self.y += (self.settings.target_speed * self.settings.fleet_direction)
        self.rect.y = self.y

    def check_edges(self):
        """Return True of target is at the top or bottom edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= screen_rect.top:
            return True

