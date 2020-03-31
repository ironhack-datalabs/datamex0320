# Game imports

import pygame as pg
from pygame.locals import *
from game_settings import *
from sprites import *


class Game:
	def __init__(self):
		# Initialize game window
		pg.init() 
		#pg.mixer.init()
		self.screen = pg.display.set_mode(SCREEN_SIZE, 0, 32) 
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.running = True
		self.camera = self.screen.get_rect()
		self.camera.x = 0

	def new(self):
		# Start a new game
		self.all_sprits = pg.sprite.Group()
		self.platforms = pg.sprite.Group()
		self.player = Player(self)
		self.all_sprits.add(self.player)
		for plat in PLATFORM_LIST:
			p = Platform(*plat)
			self.all_sprits.add(p)
			self.platforms.add(p)
		self.run()


	def run(self):
		# Game loop
		self.playing = True

		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			pg.display.update()
			self.draw()

	def update(self):
		# Game loop - Update
		self.all_sprits.update()
		self.update_camera()

		# Check if a player hits a platform - only if falling
		if self.player.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player, self.platforms, False)
			if hits:
				if self.player.pos.y > (hits[0].rect.top):
					self.player.pos.y = hits[0].rect.top
					self.player.vel.y = 0





		# Chek for player movoment in the world
		#if self.player.rect.right >= SCREEN_WIDTH*3/4:
		#	self.player.pos.x -= abs(self.player.vel.x)
		#	for plat in self.platforms:
		#		plat.rect.x -= abs(self.player.vel.x)

		while self.player.rect.left < 0:
			self.player.rect.left += 10
			self.player.vel.x = 0

		while self.player.rect.right > SCREEN_WIDTH:
			self.player.rect.right-= 10
			self.player.vel.x = 0

		while self.player.rect.left < 0 and self.player.rect.bottom > (SCREEN_HEIGTH-40):
			self.player.rect.right += 20
			self.player.rect.bottom += 50
			self.player.vel.x = 0
			#self.player
			#for plat in self.platforms:
				#plat.rect.x -= abs(self.player.vel.x)


	def events(self):
		# Game loop - Events
		for event in pg.event.get(): # Event loop
			if event.type == QUIT: # Check for window quit
				if self.playing:
					self.playing = False
				self.running = False


			if event.type == KEYDOWN:
				if event.key == K_UP:
					self.player.jump()


			#if event.type == KEYUP:
			#	if event.key == K_RIGHT:
			#		moving_right = False
			#	if event.key == K_LEFT:
			#		moving_left = False


	def draw(self):
		# Game loop - Draw
		self.screen.fill(BLACK)
		self.all_sprits.draw(self.screen)
		pg.display.flip()


	def show_start_screen(self):
		# Game startt screen 
		pass


	def show_gover_screen(self):
		# Game over screen
		pass


	def update_camera(self):
		
		ref_cam_pos = self.camera.x + self.camera.w//3

		if self.player.vel.x > 0 and self.player.pos[0] > ref_cam_pos:
			mult = 0.5 if self.player.rect.right < self.camera.centerx else 1
			new = self.camera.x + mult * self.player.vel.x
			highest = SCREEN_WIDTH - self.camera.w
			self.camera.x = min(highest, new)



g = Game()
g.show_start_screen()

while g.running:
	g.new()
	g.show_start_screen()

pg.quit()