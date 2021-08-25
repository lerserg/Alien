import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class for ship control"""

    def __init__(self, game) -> None:
        """Initializes ship and defines his position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(self.settings.ship_img)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
        self.shooting = False

    def update(self):
        """Updates ship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def draw_ship(self):
        """Draws ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Replaces ship to center """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
