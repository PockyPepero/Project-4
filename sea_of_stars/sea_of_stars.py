import sys
import pygame
from settings import Settings
from stars import Star
from random import randint

class SeaofStars():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # fullscreen mode. remove comments to enable fullscreen mode.
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
        # # tells pygame to find the window size to fill the screen
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sea of Stars")

        self.stars = pygame.sprite.Group()

        self._create_sea()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._update_screen()
 

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

    def _create_sea(self):
        """Create the sea of stars."""
        # Make a star and find the num. of stars in a row.
        # Spacing between each star is equal to one star width.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit on the screen.
        available_space_y = ((self.settings.screen_height) - 
            (3 * star_height))
        number_rows = available_space_y // (2 * star_height)

        # Create the full sea of stars.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star.rect.height * row_number
        self.stars.add(star)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SeaofStars()
    ai.run_game()