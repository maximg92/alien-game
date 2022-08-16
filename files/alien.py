import pygame
import glob
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in a fleet."""
    def __init__(self, ai_game):
        # Initialize the alien and set its starting position.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image and set its rect attribute

        # pathnfile = 'images/*.bmp'
        # image_list = glob.glob(pathnfile)
        # for img in image_list:
            # self.image = pygame.image.load(img)
            # self.rect = self.image.get_rect()

        self.image = pygame.image.load('images/seed-f.bmp')
        self.rect = self.image.get_rect()


        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien hits the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

