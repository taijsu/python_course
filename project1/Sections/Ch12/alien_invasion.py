import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
	pygame.init()
	# ver1 screen = pygame.display.set_mode((1200, 800))
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")


	bg_color = (230, 230, 230)

	# Make a ship.
	ship = Ship(ai_settings, screen)
	# Make a group to store bullets
	bullets = Group()


	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)
		

run_game()


