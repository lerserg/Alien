from time import sleep
from game_stats import GameStats
from alien import Alien
import pygame
from pygame.constants import QUIT
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from button import Button


class AlienInvation:

    def __init__(self) -> None:

        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien invation')
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, 'Play')

    def run(self):
        """Runs games main loop"""
        while True:
            self._check_events()
            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _create_fleet(self):
        """Create fleet"""
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        aliens_quantity_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height)
        row_quantity = available_space_y // (2 * alien_height)
        for row_number in range(row_quantity - 1):
            for alien_number in range(aliens_quantity_x):
                self._create_alien(alien_width, alien_height,
                                   row_number, alien_number)

    def _create_alien(self, alien_width, alien_height, row_number, alien_number):
        """Creates alien"""
        alien = Alien(self)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _control_fleet_direction(self):
        """Controls reaching the edge """
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Changes fleet direction and altitude"""
        for alien in self.aliens:  # .sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= - 1

    def _update_bullets(self):
        """Check bullets position and removes flow away"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        self._check_alien_bullet_collision()

    def _check_alien_bullet_collision(self):
        """Cheks the collisions of bullets with aliens"""
        pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _check_alien_ship_collision(self):
        """Check collision of ship with aliens """
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _check_aliens_bottom(self):
        """Check collision of aliens with ground """
        screen_bot = self.screen.get_rect().bottom
        for alien in self.aliens:
            if alien.rect.bottom > screen_bot:
                self._ship_hit()

    def _update_aliens(self):
        """Controls fleet direction and updates aliens position"""
        self._control_fleet_direction()
        self._check_alien_ship_collision()
        self._check_aliens_bottom()
        self.aliens.update()

    def _ship_hit(self):
        """Handling collision of ship with aliens"""
        sleep(0.5)
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()

    def _update_screen(self):
        """Updating screen image"""
        self.screen.fill(color=self.settings.bg_color)
        self.ship.draw_ship()
        for bullet in self.bullets:  # .sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        if self.stats.game_active == False:
            self.play_button.draw_button()
        pygame.display.flip()

    def _check_events(self):
        """Process events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown(self, event):
        """Checks the pressed button"""
        if event.key == pygame.K_p:
            self.start_game()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullets_allowed:
                self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup(self, event):
        """Checks the reliased button"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.start_game()

    def start_game(self):
        self.settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        self.stats.game_active = True
        self.stats.reset_stats()
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()

    def _fire_bullet(self):
        """Create bullet"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


if __name__ == '__main__':
    game = AlienInvation()
    game.run()
