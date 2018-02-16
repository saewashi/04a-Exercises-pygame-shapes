#!/usr/bin/env python
'''

I tried with this one, but the two drawing exercises are kind of difficult for me to understand.
And it keeps saying I am making indentions and tabs inconsistent.

'''
import sys, pygame, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

screen_size = (800,600)
FPS = 60
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
dark_green = (0,128,0)
yellow = (255,255,0)

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()
	shape = random.randange(4)

	(x,y,width,height) = (100,100,50,50)
     #shape = random.randrange(2)

	while True:
		clock.tick(FPS)

		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
				if int(shape) == 0:
                                pygame.draw.rect(screen, color, random.randrange(x,y,width,height))





		pygame.display.flip()

if __name__ == '__main__':
	main()
