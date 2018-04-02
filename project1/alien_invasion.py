
import pygame
from pygame.sprite import Group

from setting import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	pygame.init()
	# ver1 screen = pygame.display.set_mode((1200, 800))
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	stats = GameStats(ai_settings)

	bg_color = (230, 230, 230)

	# Make a ship.
	ship = Ship(ai_settings, screen)

	# Make a group to store bullets
	bullets = Group()

	#Make Alian
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	while True:
		gf.check_events(ai_settings, screen, ship, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()



