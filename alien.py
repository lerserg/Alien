import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Single alien class"""

    def __init__(self, game) -> None:
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load(self.settings.alien_img)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        """Updates alien position"""
        self.x += self.settings.alien_speed * self.settings.alien_direction
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if screen edge reached"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
