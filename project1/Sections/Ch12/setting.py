class Settings():

	def __init__(self):
		""" init game setting. """
		# Screen setting
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		#Ship setting
		self.ship_speed_factor = 5.0


		#Bullet
		self.bullet_speed_factor = 5
		self.bullet_width = 3
		self.bullet_height = 10
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 10


