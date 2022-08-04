import pygame
from pygame.sprite import Sprite

class FiringAlien(Sprite):
    """A class to manage the firing alien."""

    def __init__(self, ai_game):
        """Initialize the firing and its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the firing alien and get its rect.
        self.image = pygame.image.load('images/firing_alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new firing at the left center of the screen.
        self.rect.midright = self.screen_rect.midright

        # Store a decimal value for the firing alien's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the firing alien's position based on the movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the firing alien at its current location."""
        self.screen.blit(self.image, self.rect)
