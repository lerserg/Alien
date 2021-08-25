import pygame.font

class Scoreboard:

    def __init__(self, game) -> None:
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (255,255,0)
        self.font = pygame.font.SysFont(None, 50)
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_img = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw_score(self):
        self.screen.blit(self.score_img, self.score_rect)