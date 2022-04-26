import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from stats import Stats
from button import Button


def run_game():
    # Initialize game and create screen object
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Create an instance to store game statistics.
    pygame.display.set_caption("Alien invasion")
    # Make the Play button.
    play_button = Button(ai_settings, screen, "START")
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
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
                        bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button)


run_game()
