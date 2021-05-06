class GameStats:
    """Track statistics for Elephant Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game in an inactive state
        self.game_active = False
        # high score should never be reset
        self.high_score_filename = "highscore.txt"
        self.high_score = self.get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.elephants_left = self.settings.elephant_limit
        self.score = 0
        self.level = 0

    def get_high_score(self):

        try:
            with open(self.high_score_filename) as f:
                contents = f.read().strip()
        except FileNotFoundError:
            return 0
        else:
            return int(contents)
