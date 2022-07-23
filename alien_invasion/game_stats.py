class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self,ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        with open('all_time_hs.txt') as file_object:
            self.lines = file_object.readlines()
            self.high_score = self.lines[0]
        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1