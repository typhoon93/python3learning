class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (183, 186, 184)

        # Elepahnt settings

        self.elephant_limit = 2
        # bullet settings

        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        self.bullet_radius = 20

        # forrest settings (up / down)

        self.forest_move_speed = 10
        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the tree point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game."""
        self.elephant_speed = 1
        self.bullet_speed = 4
        self.tree_speed = 1

        # forest_direction of 1 represents top; -1 represents bottom
        self.forest_direction = 1

        # scoring
        self.tree_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.elephant_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.tree_speed *= self.speedup_scale

        self.tree_points = int(self.tree_points * self.score_scale)
