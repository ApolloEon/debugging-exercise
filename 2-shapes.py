#!/usr/bin/env python
import sys, logging, pygame, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

screen_size = (600,600)
FPS = 60
black = (0,0,0)
white = (255,255,255)
gravity = 0.8
imploding = 0.1

class Circle:
	pos = (-1,-1)
	radius = -1
	color = (0,0,0)
	velocity = 0
	shrinking = 0
	def __init__(self, pos, radius, color):
		self.pos = pos
		self.radius = radius
		self.color = color
	
	def draw(self,screen):
		(x,y) = self.pos
		pygame.draw.circle(screen, self.color, (int(x),int(y)), int(self.radius))

	def update(self):
		self.velocity += gravity
		self.shrinking += imploding
		self.radius -= self.shrinking
		(x,y) = self.pos
		y += self.velocity
		self.pos = (x,y)
	
	def alive(self):
		if self.pos[1] - self.radius > screen_size[1]:
			return False
		if self.radius >= 0:
			return True
		return False

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()
	
	circles = []
	while True:
		clock.tick(FPS)
		screen.fill(black)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				radius = random.randrange(200)
				r = random.randrange(255)
				g = random.randrange(255)
				b = random.randrange(255)
				circles.append(Circle(pos,radius,(r,g,b)))

		circles = [c for c in circles if c.alive()]

		for c in circles:
			c.update()
			if c.alive():
				c.draw(screen)
		
		pygame.display.flip()

if __name__ == '__main__':
	main()