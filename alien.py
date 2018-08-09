import pygame
from pygame.locals import *
import random
from color import *
import time
from constants import *
import spaceship
from spaceship import *
import enemies
from enemies import *
import bullet
from bullet import *



redbull = []
pygame.font.init()
f1 = pygame.font.SysFont('monospace', 30)

class App(object):
	def __init__(self):
		pygame.init()
		self.displaySurf, self.displayRect = self.makeScreen()
		self.score = 0
	def makeScreen(self):
		pygame.display.set_caption('Space Invaders')
		displaySurf = pygame.display.set_mode((DISPWIDTH,DISPHEIGHT)) 
		displayRect = displaySurf.get_rect()
		displaySurf.fill(NEARBLACK)
		#pygame.display.update()       ##saves memory: updates only part of display   #pygame.display.flip()    
		displaySurf.convert()    
		
		return displaySurf, displayRect
	def makePlayer(self):
		player = Spaceship()
		self.displaySurf.blit(player.image,player.rect)
	
		return player

	def makeEnemies(self):
		enemies = pygame.sprite.Group()
		enemy = Alien(random.randint(7,8),random.randint(0,7))#random.randint(7,8),random.randint(1,8))
		#self.displaySurf.blit(enemy.image,enemy.rect)
		enemy.setanimage('alien3.png')
		enemies.add(enemy)
		#array.append(enemy)
		return enemies

	def checkCollisions(self):
		#pygame.sprite.groupcollide(self.redBullets, self.enemies, True, False)
		for alien in pygame.sprite.groupcollide(self.redBullets, self.enemies, True, False).values():
			for i in redbull:

				if pygame.sprite.spritecollideany(i,self.enemies,collided=None) != None:
					pygame.sprite.spritecollideany(i,self.enemies,collided=None).setanimage('alien2.png')
					pygame.sprite.spritecollideany(i,self.enemies,collided=None).healthtime += 5000


		for alien in pygame.sprite.groupcollide(self.bullets, self.enemies, True, True).values():
			self.score += 1
		
	def gameInput(self):
		for event in pygame.event.get():
			if event.type == QUIT or (
				event.type == KEYDOWN and (event.key == K_q)):
				end = f1.render("Your total score is: " + str(self.score), False, SSCOLOR)
				self.displaySurf.fill(NEARBLACK)
				self.displaySurf.blit(end, [30,30])
				pygame.display.update()
				time.sleep(2)
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:    # Set the center to these new coords.
					self.player.rect.centerx += 80
					self.player.checkBoun()
				
				if event.key == pygame.K_a:   # Set the x coord to 300.
					self.player.rect.centerx -= 80
					self.player.checkBoun()
				
				if event.key == K_SPACE: 
					bullet = Bullet(self.player.rect, SSCOLOR, -1, 5)
					self.greenBullets.add(bullet)
					self.bullets.add(bullet)
					#self.bullets.draw(self.displaySurf)
				if event.key == pygame.K_s:
					bullet = Bullet(self.player.rect, GREEN, -1, 10)
					self.redBullets.add(bullet)
					redbull.append(bullet)
					self.bullets.add(bullet)
	


	def resetGame(self):        #at the beginning of game
		self.gameStart = True
		self.player = self.makePlayer()
		self.needToMakeEnemies = True
		self.bullets = pygame.sprite.Group()
		self.greenBullets = pygame.sprite.Group()
		self.redBullets = pygame.sprite.Group()
		self.keys = pygame.key.get_pressed()
		self.allSprites = pygame.sprite.Group()
		self.enemyBulletTimer = pygame.time.get_ticks()
		self.clock = pygame.time.Clock()
		self.fps = 40
		

	def mainloop(self):
		#while True:
			#if self.gameStart:
		counter = 0
		self.displaySurf.fill(NEARBLACK)
		self.resetGame()
		self.enemies = self.makeEnemies()
		while True:
			if counter%(10*self.fps) == 0:
				self.enemies = self.makeEnemies()
			self.allSprites.add(self.enemies)
			self.allSprites.add(self.bullets)
			self.gameInput()
			currentTime = pygame.time.get_ticks()
			self.allSprites.update(self.keys, currentTime)
			self.displaySurf.fill(NEARBLACK)
			self.checkCollisions()
			self.displaySurf.blit(self.player.image, self.player.rect)
			self.allSprites.draw(self.displaySurf)
			#print(self.score)
			pygame.display.update()
			counter += 1
			self.clock.tick(self.fps)



if __name__ == '__main__':
	app = App()
	app.mainloop()	


		
