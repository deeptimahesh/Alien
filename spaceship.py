import pygame
from pygame.locals import *
import random
from color import *
import time
from constants import *


class Spaceship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)         
		self.width = SSWIDTH
		self.height = SSHEIGHT
		#self.row = 1
		#self.column = column
		self.image = pygame.Surface((self.width, self.height))                    #image established
		self.color = SSCOLOR
		self.image.fill(self.color)
		self.rect = self.image.get_rect(topleft=(5,620))
		#self.aa = False
		#self.dd = False
		self.speed = SSSPEED
		self.vectorx = 0

	def checkBoun(self):                      #check for boundary of window, if exceeds put as extreme

		if self.rect.right > DISPWIDTH-5:
			self.rect.right = DISPWIDTH-5
			self.vectorx = 0
		elif self.rect.left < 5:
			self.rect.left = 5
			self.vectorx = 0