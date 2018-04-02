
class Settings():

	def __init__(self):
		""" init game setting. """
		# Screen setting
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		#Ship setting
		self.ship_speed_factor = 10

		#Alien setting
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10

		self.fleet_direction = 1

		#Bullet
		self.bullet_speed_factor = 35
		self.bullet_width = 3
		self.bullet_height = 10
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 10