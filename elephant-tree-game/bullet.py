import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the elephant"""

    def __init__(self, ai_game):
        """Create a bullet object at the elephants's current position."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midleft = ai_game.elephant.rect.midleft

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        # update the decimal position of the bullet.
        self.x -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""

        pygame.draw.circle(
            self.screen, self.color, (self.rect.midleft), self.settings.bullet_radius
        )
