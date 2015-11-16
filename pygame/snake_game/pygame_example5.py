import pygame

x = pygame.init()	#it initialises the pygame

#define colors
white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((800,600))	#it builds a canvas/screen to run the game
pygame.display.set_caption('MAN HUNT')

gameExit = False

#starting position of the snake
lead_x = 300
lead_y = 300

#change in position of the head of snake
lead_x_change = 0
lead_y_change = 0

#add a pygame clock for controling frames per second
clock = pygame.time.Clock()

while not gameExit:	#game loop
	for event in pygame.event.get(): 	#event handling loop
		print event
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -10
				lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = 10
				lead_y_change = 0
			elif event.key == pygame.K_UP:
				lead_y_change = -10
				lead_x_change = 0
			elif event.key == pygame.K_DOWN:
				lead_y_change = 10
				lead_x_change = 0
		if event.type == pygame.KEYUP: 	#this will stop moving the square once user lifts the key up
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				lead_x_change = 0
				lead_y_change = 0
			if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
				lead_x_change = 0
				lead_y_change = 0
			
	lead_x += lead_x_change
	lead_y += lead_y_change
	#fill the background with a colors
	gameDisplay.fill(white)
	
	gameDisplay.fill(black, rect = [lead_x,lead_y,10,10]) #this method to draw something is graphic accelerated which makes it fast
 	
	pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set
	clock.tick(10)	#defines 10 frames per second 
pygame.quit()	#it de-initialises the pygame

quit() 