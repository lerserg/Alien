import pygame.font


class Button:
    """Create button class"""

    def __init__(self, game, msg) -> None:
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = 200
        self.height = 100
        self.button_color = (70, 130, 180)
        self.text_color = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.font = pygame.font.SysFont(None, 48)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_img = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
