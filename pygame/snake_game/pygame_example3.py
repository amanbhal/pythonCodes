import pygame

x = pygame.init()	#it initialises the pygame

#define colors
white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((800,600))	#it builds a canvas/screen to run the game
pygame.display.set_caption('MAN HUNT')

gameExit = False

while not gameExit:
	for event in pygame.event.get():
		print event
		if event.type == pygame.QUIT:
			gameExit = True
	
	#fill the background with a colors
	gameDisplay.fill(white)
	
	#make some rectangles
	pygame.draw.rect(gameDisplay,black,[400,300,400,300])
	gameDisplay.fill(white, rect = [600,400,50,50]) #this method to draw something is graphic accelerated which makes it fast
	
	pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set

pygame.quit()	#it de-initialises the pygame

quit() 