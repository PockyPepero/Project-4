import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from target import Target 
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # fullscreen mode. remove comments to enable fullscreen mode.
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
        # tells pygame to find the window size to fill the screen
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()

        self._create_target()

        # Make the play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_targets()
                
            self._update_screen()
 
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining targets and bullets.
            self.targets.empty()
            self.bullets.empty()

            # Create a new target and center the ship.
            self._create_target()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < (self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
                self.stats.miss_count += 1

        self._check_bullet_target_collisions()

        if self.stats.miss_count == 3:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_bullet_target_collisions(self):
        # Check for any bullets that have hit aliens.
        # Removes the bullet + target upon collision.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.targets, True, True
        )

        if not self.targets:
            # Destroy existing bullets and create new target.
            self.bullets.empty()
            self._create_target()
            self.settings.increase_speed()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for target in self.targets.sprites():
            target.draw_target()

        if not self.stats.game_active:
            self.play_button.draw_button()
    
        pygame.display.flip()

    def _create_target(self):
        """Create a target."""
        target = Target(self)
        target_width, target_height = target.rect.size
        target.x = self.settings.screen_width - 2*target_width
        target.rect.x = target.x 
        target.y = target_height
        target.rect.y = target.y
        self.targets.add(target)

    def _check_target_edges(self):
        """Respond appropriately if the target has reached an edge."""
        for target in self.targets.sprites():
            if target.check_edges():
                self._change_direction()
                break

    def _change_direction(self):
        """Change the target's direction."""
        self.settings.fleet_direction *= -1

    def _update_targets(self):
        """
        Check if target is at the edge, 
        then update the position of the target.
        """
        self._check_target_edges()
        self.targets.update()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
