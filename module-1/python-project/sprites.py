# Sprites classes for the game 'King of the Jungle'
import pygame as pg
from game_settings import *
from pygame.locals import *
vec = pg.math.Vector2


monkey_mr = pg.image.load('images/monkey_r.png')
monkey_mr = pg.transform.rotozoom(monkey_mr, 0 , 1/10)

monkey_ml = pg.image.load('images/monkey_l.png')
monkey_ml = pg.transform.rotozoom(monkey_ml, 0 , 1/10)

class Player(pg.sprite.Sprite):
	image = None

	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		self.game = game

		if Player.image is None:
			Player.image = monkey_mr

		self.image = Player.image
		
		self.rect = self.image.get_rect()
		self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGTH/2)
		self.pos = vec(SCREEN_WIDTH//5, SCREEN_HEIGTH - 40)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)



	def jump(self):
		# Jump only if standing on something
		self.rect.y += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.y -= 1

		if hits:
			self.vel.y = PLAYER_JUMP



	def update(self):
		self.acc = vec(0, GRAVITY) 		
		keys = pg.key.get_pressed()

		if keys[K_LEFT]:
			Player.image = monkey_ml
			self.image = Player.image
			self.acc.x = -PLAYER_ACC
			
		if keys[K_RIGHT]:
			Player.image = monkey_mr
			self.image = Player.image
			self.acc.x = PLAYER_ACC
			
		# Apply friction
		self.acc.x += self.vel.x * PLAYER_FRICTION

		# Equations of motion
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc


		self.rect.midbottom = self.pos




class Platform(pg.sprite.Sprite):
	def __init__(self, x, y, w, h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y		
		self.rect.h = h
