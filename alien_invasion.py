import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from stats import Stats


def run_game():
    # Initialize game and create screen object
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Create an instance to store game statistics.
    pygame.display.set_caption("Alien invasion")
    ship = Ship(screen, ai_settings)
    # Make a group to store bullets in
    bullets = Group()
    # Make an alien.
    aliens = Group()
    # Add stats to the game
    stats = Stats()
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens)
    # Start the main loop for game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()
