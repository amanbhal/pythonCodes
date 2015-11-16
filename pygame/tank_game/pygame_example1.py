import pygame
import time
import random

x = pygame.init()	#it initialises the pygame

#define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600
FPS = 15 #frames per second variable

gameDisplay = pygame.display.set_mode((display_width,display_height))	#it builds a canvas/screen to run the game
pygame.display.set_caption('TANK FIGHT')
#icon = pygame.image.load('icon.jpg')
#pygame.display.set_icon(icon)	#set the icon

#add a pygame clock for controling frames per second
clock = pygame.time.Clock()

#adding font
smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",75)

#snake_img = pygame.image.load('snakehead.png')
#apple_img = pygame.image.load('apple.jpg')

def text_objects(msg,color,size):
	if size=="small":
		textSurface = smallfont.render(msg,True,color)
	elif size=="medium":
		textSurface = medfont.render(msg,True,color)
	elif size=="large":
		textSurface = largefont.render(msg,True,color)
	return textSurface, textSurface.get_rect()
	
def display_score(score):
	text = smallfont.render("Score:"+str(score),True,red)
	gameDisplay.blit(text, [0,0])
	
def message_to_screen(msg,color,y_displace=0,size="small"):	#we set the y axis displace of the text sent to this function
	textSurf, textRect = text_objects(msg,color,size)	#textRect is the rectangle around the text
	textRect.center = (display_width/2),(display_height/2)+y_displace	#to center the text we center the rectangle around the text
	gameDisplay.blit(textSurf,textRect)

def game_intro():
		intro = True
		while intro:
			gameDisplay.fill(black)
			message_to_screen("TANK FIGHT",red,y_displace=-100,size="large")
			message_to_screen("Destroy the enemy tanks with your tank",white)
			message_to_screen("Press P to Play the game",red,y_displace=100,size="medium")
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						intro = False
						game_loop()
						
def pause():
	paused = True
	
	while paused:
		#gameDisplay.fill(black)  #commenting this will enable u to see the back screen of the game 
		message_to_screen("Game Paused",red,y_displace=-100,size="large")
		message_to_screen("Press C to continue or Q to quit",green)
		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
						
def game_loop():
	
	gameExit = False
	gameOver = False
	score = 0
	
	while not gameExit:
	
		while gameOver == True:
			#gameDisplay.fill(black)
			message_to_screen("GAME OVER!",red,y_displace = -50,size="large")
			message_to_screen("Your Score:"+str(score),red,y_displace=25)
			message_to_screen("Press C to continue or Q to quit",green,y_displace=100)
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						game_loop()
					elif event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					
		for event in pygame.event.get(): 	#event handling loop
			#print event
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pass
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_RIGHT:
					pass
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					pass
					
		#fill the background with a colors
		gameDisplay.fill(white)
		display_score(score)
		pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set
		
		clock.tick(FPS)	#defines 10 frames per second

	pygame.quit()	#it de-initialises the pygame

	quit() 
	
game_intro()