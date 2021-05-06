import pygame
from pygame.sprite import Sprite


class Tree(Sprite):
    """A class to represent a single tree in a forest"""

    def __init__(self, ai_game):
        """Initialize the treee and set it's starting position."""

        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the tree image and set it's rect attribute

        self.image = pygame.image.load("images/tree.bmp")
        self.rect = self.image.get_rect()

        # Start each new tree near the top left of the screen.

        self.rect.y = self.rect.height
        self.rect.x = self.rect.width

        # store the alien's exact vertical position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if a tree is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Move the trees down"""
        self.y += self.settings.tree_speed * self.settings.forest_direction
        self.rect.y = self.y
