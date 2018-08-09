import pygame
from pygame.locals import *
import random
from color import *
import time
from constants import *


class Alien(pygame.sprite.Sprite):
	def __init__(self,row,column):
		pygame.sprite.Sprite.__init__(self)
		self.width = ENEMYWIDTH
		self.height = ENEMYHEIGHT
		self.row = row
		self.column = column
		#self.image = self.setanimage('alien3.png')
		#self.rect = self.image.get_rect(topleft=((20 + self.column*80, 650 - (self.row*80))))
		self.vectorx = 1
		self.healthtime = 10000
		self.timeOffset = row * TIMEOFFSET
		self.timer = pygame.time.get_ticks() - self.timeOffset
		self.score = 0
	def update(self, keys, currentTime):
		if currentTime - self.timer > self.healthtime:
			self.kill()
					
	def setanimage(self, file):
		self.image = pygame.image.load(file)
		self.image.convert_alpha()
		self.image = pygame.transform.scale(self.image,(self.width, self.height))
		#return image
		self.rect = self.image.get_rect(topleft=((20 + self.column*80, 650 - (self.row*80))))