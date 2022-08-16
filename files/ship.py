import pygame
import glob
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.

        ### pathnfile = 'images/*.bmp'
        ### image_list = glob.glob(pathnfile)
        ### for img in image_list:
        ### copy self.image = pygame.image.load('images/zh-f.bmp')
        ### copy self.rect = self.image.get_rect()

        self.image = pygame.image.load('images/zh-f.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Draw ship at its current location
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Define the ship's position based on movement flag."""
        # Update the ship's x value, not the rect:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """Centers the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
