import pygame
from pygame.sprite import Sprite


class Elephant(Sprite):
    """A class to manage the elephant."""

    def __init__(self, ai_game):
        """Initialize the elephant and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the elephant image and get its rect

        self.image = pygame.image.load("images/elephant.bmp")
        self.rect = self.image.get_rect()

        # Start each new elephant at the top of the screen
        self.rect.midright = self.screen_rect.midright

        # store a decimal value for the ship's horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the elephant's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.elephant_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.elephant_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.elephant_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.elephant_speed

        # updaate rect object from self.x / self.yield
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the Elephant at it's current location."""
        self.screen.blit(self.image, self.rect)

    def center_elephant(self):
        """Center the elephant on the screen."""
        self.rect.midright = self.screen_rect.midright
        self.x = float(self.rect.x)
