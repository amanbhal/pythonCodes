# adding object collision i.e. crossing over objects. Let's make our apple bigger and make the crossover
#here the crossover can be slight i.e. the nake is not fully inside the apple 
#we also centered the text
import pygame
import time
import random

x = pygame.init()	#it initialises the pygame

#define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600
FPS = 15 #frames per second variable

gameDisplay = pygame.display.set_mode((display_width,display_height))	#it builds a canvas/screen to run the game
pygame.display.set_caption('MAN HUNT')


#add a pygame clock for controling frames per second
clock = pygame.time.Clock()

#adding font
font = pygame.font.SysFont(None,25)

def display_snake(block_size,snakelist):
	for XnY in snakelist:
		gameDisplay.fill(black, rect = [XnY[0],XnY[1],block_size,block_size]) #this method to draw something is graphic accelerated which makes it fast

def text_objects(msg,color):
	textSurface = font.render(msg,True,color)
	return textSurface, textSurface.get_rect()
	
def message_to_screen(msg,color):
	textSurf, textRect = text_objects(msg,color)	#textRect is the rectangle around the text
	textRect.center = (display_width/2),(display_height/2)	#to center the text we center the rectangle around the text
	gameDisplay.blit(textSurf,textRect)
def game_loop():
	gameExit = False
	gameOver = False

	#starting position of the snake
	lead_x = display_width/2
	lead_y = display_height/2

	#change in position of the head of snake
	lead_x_change = 0
	lead_y_change = 0

	block_size = 20
	appleSize = 40 	#making apple bigger
	snakelist = []
	snakelength = 1
	#positioning apple at a random place and indenting it with the snake using round function
	appleX = round(random.randrange(0,display_width-appleSize))#/10.0)*10.0
	appleY = round(random.randrange(0,display_height-appleSize))#/10.0)*10.0

	while not gameExit:
	
		while gameOver == True:
			gameDisplay.fill(black)
			message_to_screen("GAME OVER! Press C to continue or Q to quit",red)
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						game_loop()
					elif event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					
		for event in pygame.event.get(): 	#event handling loop
			print event
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				if event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				if event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				if event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0
					
		#set boundary conditions
		if lead_x>=display_width or lead_x<=0 or lead_y<=0 or lead_y>=display_height:
			gameOver = True
		
		#make the snake continue to move after pressing an arrow key
		lead_x += lead_x_change
		lead_y += lead_y_change
		
		#make the snake a list of blocks
		snakehead = []
		snakehead.append(lead_x)
		snakehead.append(lead_y)
		snakelist.append(snakehead)
		
		#fill the background with a colors
		gameDisplay.fill(white)
		gameDisplay.fill(red, rect=[appleX,appleY,appleSize,appleSize])
		if len(snakelist)>snakelength:
			del snakelist[0]
		#gameover if the snake runs into himself
		for eachSegment in snakelist[:-1]:	#upto last element bcoz last element is head
			if eachSegment == snakehead:
				gameOver = True
				
		display_snake(block_size,snakelist)
		pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set
		
		if (lead_x >= appleX and lead_x<=appleX+appleSize) or (lead_x+block_size>=appleX and lead_x+block_size<=appleX+appleSize):
			if (lead_y >= appleY and lead_y<=appleY+appleSize) or (lead_y+block_size>=appleY and lead_y+block_size<=appleY+appleSize):	#generate a new apple wenever we eat an apple
				appleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
				appleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
				snakelength += 1

		
		clock.tick(FPS)	#defines 10 frames per second

	pygame.quit()	#it de-initialises the pygame

	quit() 
	
game_loop()