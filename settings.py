import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

    # Screen settings
        self.screen_width = 480
        self.screen_height = 700
        self.bg_color = (80, 97, 126)
        self.background = pygame.image.load("images/space.jpg")
    # Ship setting
        self.ship_speed_factor = 1.5
    # Bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 252, 62, 83
        self.bullets_allowed = 10000

    # Alien settings
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
