import pygame

x = pygame.init()	#it initialises the pygame

#define colors
white = (255,255,255)
black = (0,0,0)
gameDisplay = pygame.display.set_mode((800,600))	#it builds a canvas/screen to run the game
pygame.display.set_caption('MAN HUNT')
pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		print event
		if event.type == pygame.QUIT:
			gameExit = True

pygame.quit()	#it de-initialises the pygame

quit() 