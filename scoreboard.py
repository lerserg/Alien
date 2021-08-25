import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard:

    def __init__(self, game) -> None:
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 50)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.ships = Group()
        self.prep_ships()
        

    def prep_score(self):
        score_str = f'{round(self.stats.score, -1):,}'
        self.score_img = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score_str = f'{round(self.stats.high_score, -1):,}'
        self.high_score_img = self.font.render(
            high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = 20

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_img = self.font.render(
            level_str, True, self.text_color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = ship.rect.width * ship_number + 10
            ship.rect.y = 10
            self.ships.add(ship)

    def draw_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

    def check_highscore(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
