import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = self.screen_rect.top

    def prep_high_score(self):
        """Turn high score into a rendered image"""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Display high score at the top right of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left
        self.high_score_rect.top = self.screen_rect.top
    def show_score(self):
        """Draw scores and level to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Check if there is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn level number into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Display level below high score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom

    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.midtop = self.screen_rect.midtop
            ship.rect.x = (ship.rect.x - (ship.rect.width / 2 * (len(range(self.stats.ships_left))-1))) + ship_number * ship.rect.width
            self.ships.add(ship)