#!/usr/bin/env python
'''

For every line, please add a comment describing what it does.

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''
import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

screen_size = (800,600)
# screen_size sets the size of the resolution of the screen, to make sure it adjusts to the appropriaite size.
FPS = 60
# FPS sets the Frames Per Second, to make sure that the program runs or ticks a certain number of times.

def main():
	# Defines the main
	pygame.init()
	# pygame.init initalizes the pygame objects to get it started.
	screen = pygame.display.set_mode(screen_size)
	# This sets the pygame display mode to the screen size we declared earlier.
	clock = pygame.time.Clock()
	# This sets the pygame clock to show time.

	while True:
		# This is performing a Boolean statement.
		clock.tick(FPS)
		# this statement is retriving the clock and FPS, to make sure it ticks to the amount of time that was defined.
		screen.fill((0,0,0))
		# This statement fills the screen with color, which in this case is blck.

		for event in pygame.event.get():
	# This statement is performing a for statement, which is retriving the event within pygame.
			if event.type == pygame.QUIT:
				#This is performing an if statement, which is saying that if the event type equals quit, then close the program.
				# This means if the user clicks the x button on the program, it will stop running it and exit.
				pygame.quit()
				# This is stating to close or quit the pygame if an event has been perform.
				sys.exit(0)
				# this exits the program on the computer, and tells it to stop running.

		pygame.display.flip()
		# This statement is taking the pygame display, and flipping it so that it displays the pixels on the screen properly -
		# which would otherwise cause an unwanted amount of flashing of pixels on the screen.
		# This is something I like to call, the Mirror Effect.

if __name__ == '__main__':
	main()
# This statement is to call the file, by whoever is using it, so that it doesn't do its own thing, and run automatically.
