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
colors = [(134,142,150),(250,82,82),(230,73,128),(190,75,219),(121,80,242),(76,110,245),(34,138,230),(21,170,191),(18,184,134),(64,192,87),(130,201,30),(250,176,5),(253,126,20),(233,236,239),(255,236,153),(163,218,255)]	

class Circle:
	pos = (-1,-1)
	radius = -1
	color = (0,0,0)
	velocity = 0
	shrinking = 0
	imploding = 0.1
	def __init__(self, pos, radius, color, imploding):
		self.pos = pos
		self.radius = radius
		self.color = color
		self.imploding = imploding
	
	def draw(self,screen):
		(x,y) = self.pos
		pygame.draw.circle(screen, self.color, (int(x),int(y)), int(self.radius))

	def update(self):
		self.velocity += gravity
		self.shrinking += self.imploding
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
				radius = random.randrange(20,100)
				c = colors[random.randrange(len(colors))]
				i = float(random.randrange(500))/1000
				circles.append(Circle(pos,radius,c,i))

		circles = [c for c in circles if c.alive()]

		for c in circles:
			c.update()
			if c.alive():
				c.draw(screen)
		
		pygame.display.flip()

if __name__ == '__main__':
	main()