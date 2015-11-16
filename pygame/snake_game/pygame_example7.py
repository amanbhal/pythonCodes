# adding handlers for exiting the game and showing the text
import pygame
import time

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

def message_to_screen(msg,color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [display_width/2,display_height/2])
def game_loop():
	gameExit = False
	gameOver = False

	#starting position of the snake
	lead_x = display_width/2
	lead_y = display_height/2

	#change in position of the head of snake
	lead_x_change = 0
	lead_y_change = 0

	block_size = 10

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
		
		#fill the background with a colors
		gameDisplay.fill(white)
		
		gameDisplay.fill(black, rect = [lead_x,lead_y,block_size,block_size]) #this method to draw something is graphic accelerated which makes it fast
		
		pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set
		clock.tick(FPS)	#defines 10 frames per second

	pygame.quit()	#it de-initialises the pygame

	quit() 
	
game_loop()