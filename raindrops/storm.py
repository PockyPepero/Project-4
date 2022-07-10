import sys
import pygame
from settings import Settings
from raindrops import Raindrop

class Storm():
    """Overall class to manage raindrops."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Storm")

        self.raindrops = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._update_raindrops()
            self._update_screen()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of raindrops."""
        # Make a raindrop and find the num. of raindrops in a row.
        # Spacing between each raindrop is equal to one raindrop width.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - (2 * raindrop_width)
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit on the screen.
        available_space_y = self.settings.screen_height 
        number_rows = available_space_y // (2 * raindrop_height)

        # Create the full fleet of raindrops.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create a raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop_height + (2 * raindrop.rect.height * row_number)
        self.raindrops.add(raindrop)

    def _check_fleet_edges(self):
        """Respond appropriately if a row of raindrops reaches the bottom."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                #self.raindrops.remove(raindrop)
                #self._create_new_row()
                raindrop.y = 0
                raindrop.rect.y = 0
                self._make_fleet_fall()

    def _make_fleet_fall(self):
        """Makes the fleet of raindrops fall."""
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += self.settings.raindrop_speed

    def _update_raindrops(self):
        """
        Check if fleet is at the edge, 
        then update the positions of all raindrops in the fleet.
        """
        self._check_fleet_edges()
        self._make_fleet_fall()
        

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Storm()
    ai.run_game()






