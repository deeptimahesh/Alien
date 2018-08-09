import pygame
from pygame.locals import *
import random
from color import *
import time
from constants import *

class Bullet(pygame.sprite.Sprite):
	def __init__(self,rect,color,vectory,speed):
		pygame.sprite.Sprite.__init__(self)
		self.width = BULLETWIDTH
		self.height = BULLETHEIGHT
		self.color = color
		self.image = pygame.Surface((self.width,self.height))
		self.image.fill(self.color)
		self.rect = self.image.get_rect()#midbottom=((rect.top , rect.top - 80)))
		self.rect.centerx = rect.centerx 
		self.rect.top = rect.bottom 
		self.vectory = vectory
		self.speed = speed
	def update(self, *args):
		self.oldLocation = (self.rect.x, self.rect.y)
		self.rect.y += self.vectory * self.speed
		#if self.rect.bottom > 600:
			#self.kill()