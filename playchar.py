import pygame

class PlayChar:
    """A class to manage the player character."""

    def __init__(self, ai_game):
        """Initialize the player character and their starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character and get its rect.
        self.image = pygame.image.load('images/guy.bmp')
        self.rect = self.image.get_rect()

        # Start each new player character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at their current location."""
        self.screen.blit(self.image, self.rect)