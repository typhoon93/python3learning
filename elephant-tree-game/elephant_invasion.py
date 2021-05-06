import sys
from time import sleep

import pygame
from random import randint


from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from elephant import Elephant
from bullet import Bullet
from tree import Tree
from button import Button


class ElephantInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """initialize the game, and create game resources."""

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Elephant Invasion")

        # Create an instance to share game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.elephant = Elephant(self)
        self.bullets = pygame.sprite.Group()
        self.trees = pygame.sprite.Group()
        self._create_forest()

        # make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:

                self.elephant.update()
                self._update_bullets()
                self._update_trees()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self._write_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.elephant.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.trees.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # draw the play button
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_forest(self):
        """Create the forest of trees."""
        # Make a tree and find the number of trees in a column
        # Spacing between each tree is qual to one tree height
        tree = Tree(self)
        tree_width, tree_height = tree.rect.size
        available_space_y = self.settings.screen_height - (2 * tree_height)
        number_trees_y = int(available_space_y // (1.5 * tree_height))

        # Determine the number of columns of trees that fit into the screen
        elephant_width = self.elephant.rect.width

        available_space_x = (
            self.settings.screen_width - (3 * tree_width) - elephant_width
        )
        number_cols = available_space_x // (2 * tree_width)
        print(number_cols)

        # create the full forest of trees
        for col_number in range(number_cols):
            for tree_number in range(number_trees_y):
                self._create_tree(tree_number, col_number)

    def _create_tree(self, tree_number, col_number):
        """Create a tree and place it in a column"""

        tree = Tree(self)
        tree_width, tree_height = tree.rect.size

        # getting the position of the tree + adding a randomness factor to the Y axis
        tree.y = tree_height + 2 * tree_height * tree_number + randint(-50, 50)
        tree.rect.y = tree.y
        tree.rect.x = tree_width + 2 * tree_width * col_number
        self.trees.add(tree)

    def _update_trees(self):
        """Update the position of all trees in the forest."""
        self._check_forest_edges()
        self.trees.update()

        # look for tree-elephant collisions
        if pygame.sprite.spritecollideany(self.elephant, self.trees):
            self._elephant_hit()

        # Look for trees hitting the bottom of the screen.
        self._check_trees_bottom()

    def _check_forest_edges(self):
        """Respond appropriatele if any trees have reached an edge."""
        for tree in self.trees.sprites():
            if tree.check_edges():
                self._change_forest_direction()
                break

    def _change_forest_direction(self):
        """Move the entire forest and change the forest's direction."""
        for tree in self.trees.sprites():
            tree.rect.x += self.settings.forest_move_speed

        self.settings.forest_direction *= -1

    def _check_keydown_event(self, event):
        """respond to keypresses."""

        if event.key == pygame.K_RIGHT:
            self.elephant.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.elephant.moving_left = True
        elif event.key == pygame.K_UP:
            self.elephant.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.elephant.moving_down = True
        elif event.key == pygame.K_q:
            self._write_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._check_play_button("pressedP")

    def _check_keyup_event(self, event):
        """Respond to key releases"""

        if event.key == pygame.K_RIGHT:
            self.elephant.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.elephant.moving_left = False
        elif event.key == pygame.K_UP:
            self.elephant.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.elephant.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # update bullet positions.
        self.bullets.update()

        # get rid of bullets that have disappeared

        for bullet in self.bullets.copy():
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_tree_collisions()

    def _check_bullet_tree_collisions(self):

        # Check forr any bullets that have hit trees
        # if so, get rid of the bullets and the tree

        collisions = pygame.sprite.groupcollide(self.bullets, self.trees, True, True)

        if collisions:
            # check if multiple trees were hit by the same bullet
            for trees in collisions.values():
                self.stats.score += self.settings.tree_points * len(trees)

            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.trees:
            # Destroy existing bullets and create new forest
            self.bullets.empty()
            self._create_forest()
            self.settings.increase_speed()

            # increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _elephant_hit(self):
        """Respond to the elephant being hit by a tree."""

        if self.stats.elephants_left > 0:

            self.stats.elephants_left -= 1
            self.sb.prep_elephants()

            # Get rid of remaining trees and bullets.
            self.trees.empty()
            self.bullets.empty()

            # Create a new fleet and center the elephant

            self._create_forest()
            self.elephant.center_elephant()

            # pause
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_trees_bottom(self):
        """Check if any trees have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for tree in self.trees.sprites():
            if tree.rect.right >= screen_rect.right:
                # Treat the same as if the elephant got hit
                self._elephant_hit()
                break

    def _check_play_button(self, action_taken):
        """Start a new game when the player clicks Play."""

        if action_taken != "pressedP":
            button_clicked = self.play_button.rect.collidepoint(action_taken)
        else:
            button_clicked = False
        if (
            button_clicked or action_taken == "pressedP"
        ) and not self.stats.game_active:
            # reset the game settings.
            self.settings.initialize_dynamic_settings()

            # reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_elephants()

            # get rid of any remaining trees and bullets
            self.trees.empty()
            self.bullets.empty()

            # create a new forest and center the elephant
            self._create_forest()
            self.elephant.center_elephant()

            # hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _write_high_score(self):
        with open(self.stats.high_score_filename, "w") as f:
            f.write(str(self.stats.high_score))


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = ElephantInvasion()
    ai.run_game()
