# adding controls screen
# drawing and moving tank
import pygame
import time
import random
import math

x = pygame.init()	#it initialises the pygame

#define colors
white = (255,255,255)
black = (0,0,0)
red = (155,0,0)
green = (0,155,0)
yellow = (150,150,0)
lightred = (255,0,0)
lightgreen = (0,255,0)
lightyellow = (255,255,0)

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


tankWidth = 45
tankHeight = 20
turret = int(tankHeight)/2

turretWidth = 5		#width of gun
turretLength = 20	#length of gun
wheelWidth = 5

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
	
def display_button(text,inactivecolor,activecolor,buttonx,buttony,buttonwidth,buttonheight,action):
	# draw buttons as rectangles
	# make the button lighter in color if the mouse hovers above it
	cur = pygame.mouse.get_pos()	# 'cur' is a tuple with x and y positions of the mouse
	click = pygame.mouse.get_pressed()	# 'click' is the tuple which hold (1,0,0) if left button on mouse is click and (0,1,0) is center button i clicked and (0,0,1) if reight button is clicked
	
	if cur[0]>buttonx and cur[0]<buttonx+buttonwidth and cur[1]>buttony and cur[1]<buttony+buttonheight:
		pygame.draw.rect(gameDisplay,activecolor,(buttonx,buttony,buttonwidth,buttonheight))
		if click[0]==1 and action=="play":	#i.e left mouse buttton is clicked when mouse pointer is inside the button region
			game_loop()
		elif click[0]==1 and action=="controls":
			game_controls()
		elif click[0]==1 and action=="quit":
			pygame.quit()
			quit()
	else:
		pygame.draw.rect(gameDisplay,inactivecolor,(buttonx,buttony,buttonwidth,buttonheight))
	
	#display text on buttons
	text_to_button(text,black,buttonx,buttony,buttonwidth,buttonheight)
	
def text_to_button(text,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):
	textSurf, textRect = text_objects(text,color,size)
	textRect.center = (buttonx+buttonwidth/2),(buttony+buttonheight/2)
	gameDisplay.blit(textSurf,textRect)
	
def message_to_screen(msg,color,y_displace=0,size="small"):	#we set the y axis displace of the text sent to this function
	textSurf, textRect = text_objects(msg,color,size)	#textRect is the rectangle around the text
	textRect.center = (display_width/2),(display_height/2)+y_displace	#to center the text we center the rectangle around the text
	gameDisplay.blit(textSurf,textRect)

def game_controls():	
	show = True
	while show:
		gameDisplay.fill(black)
		message_to_screen("CONTROLS",lightred,y_displace=-100,size="large")
		#message_to_screen("Destroy the enemy tanks with your tank",white,-30)
		message_to_screen("Fire: Spacebar",white,10)
		message_to_screen("Move Turret: UP and DOWN arrow key",white,50)
		message_to_screen("Move Tank: LEFT and RIGHT arrow key",white,90)
		message_to_screen("Pause: Press P",white,130)
		
		#display buttons
		display_button("Play",green,lightgreen,100,500,100,50,action="play")
		#display_button("Controls",yellow,lightyellow,350,500,100,50,action="controls")
		display_button("Quit",red,lightred,600,500,100,50,action="quit")
			
		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
def game_intro():
		intro = True
		while intro:
			gameDisplay.fill(black)
			message_to_screen("TANK FIGHT",lightred,y_displace=-100,size="large")
			message_to_screen("Destroy the enemy tanks with your tank",white)
			
			#display buttons
			display_button("Play",green,lightgreen,100,400,100,50,action="play")
			display_button("Controls",yellow,lightyellow,350,400,100,50,action="controls")
			display_button("Quit",red,lightred,600,400,100,50,action="quit")
				
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
						
def display_tank(x,y,turretAngle=math.radians(45)):
	x = int(x)
	y = int(y)
	# drawing turret
	pygame.draw.circle(gameDisplay,black,(x,y),turret)
	# drawing tank body
	pygame.draw.rect(gameDisplay,black,(x-int(tankWidth)/2,y,tankWidth,tankHeight))
	# drawing turret gun
	pygame.draw.line(gameDisplay,black,(x,y),(x-(turretLength*math.cos(turretAngle)),y-(turretLength*math.sin(turretAngle))),turretWidth)
	
	# drawing wheels
	startWheelX = int(tankWidth)/2
	for i in range(4):
		pygame.draw.circle(gameDisplay,black,(x-startWheelX,y+tankHeight+5),wheelWidth)
		startWheelX -= wheelWidth*3

def game_loop():
	
	gameExit = False
	gameOver = False
	score = 0
	
	# starting position of the main tank
	mainTankX = display_width * 0.9
	mainTankY = display_height *0.9
	turretAngle = math.radians(45)	#starting angle of gun from -x axis in clockwise direction
	tankMove = 0					#steps tank move when we press arrow keys
	turretMove = math.radians(0)	#angle gun rotate when we press arrow keys
	
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
		
		# move tank left and right
		for event in pygame.event.get(): 	#event handling loop
			#print event
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					tankMove -= 5
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_RIGHT:
					tankMove += 5
				elif event.key == pygame.K_UP:
					turretMove = math.radians(2)
				elif event.key == pygame.K_DOWN:
					turretMove = math.radians(-2)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					tankMove = 0
				elif event.key == pygame.K_RIGHT:
					tankMove = 0
				elif event.key == pygame.K_UP:
					turretMove = math.radians(0)
				elif event.key == pygame.K_DOWN:
					turretMove = math.radians(0)
		
		mainTankX += tankMove
		turretAngle += turretMove
		#fill the background with a colors
		gameDisplay.fill(white)
		# display tank
		display_tank(mainTankX,mainTankY,turretAngle)
		display_score(score)
		pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set
		
		clock.tick(FPS)	#defines 10 frames per second

	pygame.quit()	#it de-initialises the pygame

	quit() 
	
game_intro()