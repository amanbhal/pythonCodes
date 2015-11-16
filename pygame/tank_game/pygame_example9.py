# drawing health bars and damage

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

#set game window height and width
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
blast = pygame.image.load("blast.png")
barrier_blast = pygame.transform.rotate(blast,270)
enemy_barrier_blast = pygame.transform.rotate(blast,90)

#tank dimensions
tankWidth = 50
tankHeight = 20
turret = int(tankHeight)/2

# turret dimensions
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
	
def display_power(power):
	text = smallfont.render("Power:"+str(power)+"%",True,red)
	gameDisplay.blit(text, [200,0])
	
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
	
def display_enemyTank(x,y):
	x = int(x)
	y = int(y)
	turretAngle=math.radians(70)
	# drawing turret
	pygame.draw.circle(gameDisplay,black,(x,y),turret)
	# drawing tank body
	pygame.draw.rect(gameDisplay,black,(x-int(tankWidth)/2,y,tankWidth,tankHeight))
	# drawing turret gun
	pygame.draw.line(gameDisplay,black,(x,y),(x+(turretLength*math.cos(turretAngle)),y-(turretLength*math.sin(turretAngle))),turretWidth)
	
	# drawing wheels
	startWheelX = int(tankWidth)/2
	for i in range(4):
		pygame.draw.circle(gameDisplay,black,(x-startWheelX+10,y+tankHeight+1),wheelWidth)
		startWheelX -= wheelWidth*2+1
	
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
		pygame.draw.circle(gameDisplay,black,(x-startWheelX+10,y+tankHeight+1),wheelWidth)
		startWheelX -= wheelWidth*2+1

def laser_shoot(x,y,turretAngle=math.radians(45)):
	startLaser = (x-(turretLength*math.cos(turretAngle)),y-(turretLength*math.sin(turretAngle)))
	# by simple maths we know the equation of line along which the laser will move i.e. y = tan(turretAngle)*x + c 
	#therefore we can find the other end of the line putting x = 0 in the above equation
	endLaser = (0,startLaser[1]-math.tan(turretAngle)*startLaser[0])
	pygame.draw.line(gameDisplay,lightred,startLaser,endLaser,turretWidth)

def display_barrier(xlocation,randomHeight,barrierWidth):
	pygame.draw.rect(gameDisplay,black,(xlocation,display_height-randomHeight,barrierWidth,randomHeight))

def missile_shoot(x,y,power,enemyTankX,turretAngle=math.radians(45)):
	#full jugaad wala function
	damage = 0
	fire = True
	xy = (int(x-(turretLength*math.cos(turretAngle))),int(y-(turretLength*math.sin(turretAngle))))
	
	startMissile = list(xy)
	turretAngle *= 6
	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.draw.circle(gameDisplay,lightred,(startMissile[0],startMissile[1]),5)
		
		startMissile[0] -= int((12 - (turretAngle))*2)
		startMissile[1] += int((((startMissile[0]-xy[0])*0.01/(float(power)/50))**2) - (int(turretAngle)+int(turretAngle)/(12-int(turretAngle))))
		pygame.display.update()
		
		if startMissile[1]>display_height-groundHeight:
			gameDisplay.blit(blast,[startMissile[0]-40,display_height-groundHeight-40])
			pygame.display.update()
			time.sleep(0.5)
			if enemyTankX-15 <startMissile[0] <enemyTankX+15:
				damage = 10
			fire = False
			
		if startMissile[0]>=xlocation and startMissile[0]<=xlocation+barrierWidth and startMissile[1]<=display_height and startMissile[1]>=display_height-randomHeight:
			fire = False	
			gameDisplay.blit(barrier_blast,[xlocation+barrierWidth,startMissile[1]])
			pygame.display.update()
			time.sleep(0.5)
			
		clock.tick(60)
	return damage
		
def enemy_missile_shoot(x,y,mainTankX,mainTankY):
	#full jugaad wala function
	damage = 0
	turretAngle=math.radians(70)
	xy = (int(x+(turretLength*math.cos(turretAngle))),int(y-(turretLength*math.sin(turretAngle))))
	startMissile = list(xy)
	turretAngle *= 6
	
	# in order to add artificial intelligence. We keep our turrent angle fixed to 70 degree and find the correct power needed to hit the main tank.
	powerFind = 1
	powerSearch = True
	
	while powerSearch:
		powerFind += 1
		if powerFind > 100:
			powerSearch = False
		fire = True
		while fire:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					
			startMissile[0] += int((12 - (turretAngle))*2)
			startMissile[1] += int((((startMissile[0]-xy[0])*0.01/(float(powerFind)/50))**2) - (int(turretAngle)+int(turretAngle)/(12-int(turretAngle))))

			if startMissile[1]>display_height-groundHeight:
				if mainTankX-15 < startMissile[0] < mainTankX+15:	#if the shell explodes near main tank we will stop the search for power
					powerSearch = False
					damage = 10
				fire = False
			if startMissile[0]>=xlocation and startMissile[0]<=xlocation+barrierWidth and startMissile[1]<=display_height and startMissile[1]>=display_height-randomHeight:
				fire = False
				damage = 0
				
	# now we are firing the actual shot
	fire = True
	# we need to re calculate the starting position because the upper code modified it
	xy = (int(x+(turretLength*math.cos(turretAngle))),int(y-(turretLength*math.sin(turretAngle))))
	startMissile = list(xy)
	
	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.draw.circle(gameDisplay,lightred,(startMissile[0],startMissile[1]),5)
		
		startMissile[0] += int((12 - (turretAngle))*2)
		startMissile[1] += int((((startMissile[0]-xy[0])*0.01/(float(powerFind)/50))**2) - (int(turretAngle)+int(turretAngle)/(12-int(turretAngle))))
		pygame.display.update()
		
		if startMissile[1]>display_height-groundHeight:
			gameDisplay.blit(blast,[startMissile[0]-40,display_height-groundHeight-40])
			pygame.display.update()
			time.sleep(0.5)
			if mainTankX-15 < startMissile[0] < mainTankX+15:	#if the shell explodes near main tank we will stop the search for power
				damage = 10
			fire = False
			
		if startMissile[0]>=xlocation and startMissile[0]<=xlocation+barrierWidth and startMissile[1]<=display_height and startMissile[1]>=display_height-randomHeight:
			fire = False
			damage = 0
			gameDisplay.blit(enemy_barrier_blast,[xlocation,startMissile[1]])
			pygame.display.update()
			time.sleep(0.5)
			
		clock.tick(60)
	return damage

def display_health_bars(player_health, enemy_health):
	if player_health > 75:
		player_health_color = green
	elif player_health > 50:
		player_health_color = yellow
	else:
		player_health_color = red
		
	if enemy_health > 75:
		enemy_health_color = green
	elif enemy_health > 50:
		enemy_health_color = yellow
	else:
		enemy_health_color = red	
		
	pygame.draw.rect(gameDisplay,player_health_color,(680,45,player_health,25))
	pygame.draw.rect(gameDisplay,enemy_health_color,(20,45,enemy_health,25))
		
def game_loop():
	
	gameExit = False
	gameOver = False
	score = 0
	global groundHeight
	power = 50
	powerChange = 0
	
	player_health = 100
	enemy_health = 100
	
	# starting position of the main tank
	mainTankX = display_width * 0.9	#it is the x co-ordinate of the center of the turret circle i.e. mid of the width of rectangle
	mainTankY = display_height *0.9	#it is the y co-ordinate of the center of the turret circle i.e. mid of the width of rectangle
	turretAngle = math.radians(45)	#starting angle of gun from -x axis in clockwise direction
	tankMove = 0					#steps tank move when we press arrow keys
	turretMove = math.radians(0)	#angle gun rotate when we press arrow keys
	
	#starting position of the enemy tank
	enemyTankX = display_width*0.2
	enemyTankY = display_height*0.9
	enemyTankMove = 0
	enemyTurretAngle = math.radians(45)
	enemyTurretMove = math.radians(0)
	
	groundHeight = display_height-(mainTankY+tankHeight)
	
	#barrier initializations
	global xlocation
	global randomHeight
	global barrierWidth
	xlocation = (display_width/2) + random.randint(-0.2*display_width,0.2*display_width)
	randomHeight = random.randrange(0.1*display_height,0.6*display_height)
	barrierWidth = 50
	
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
		
		# move tank left and right and shooting the laser
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
				#elif event.key == pygame.K_RCTRL:
				#	missile_shoot(mainTankX,mainTankY,power,turretAngle)
				elif event.key == pygame.K_SEMICOLON:
					powerChange = -1
				elif event.key == pygame.K_SLASH:
					powerChange = 1
				if event.key == pygame.K_a:
					enemyTankMove -= 5
				elif event.key == pygame.K_d:
					enemyTankMove += 5
				elif event.key == pygame.K_w:
					enemyTurretMove = math.radians(2)
				elif event.key == pygame.K_s:
					enemyTurretMove = math.radians(-2)
				elif event.key == pygame.K_SPACE:
					damage = missile_shoot(mainTankX,mainTankY,power,enemyTankX,turretAngle)
					enemy_health -= damage
					damage = enemy_missile_shoot(enemyTankX,enemyTankY,mainTankX,mainTankY)
					player_health -= damage
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					tankMove = 0
				elif event.key == pygame.K_RIGHT:
					tankMove = 0
				elif event.key == pygame.K_UP:
					turretMove = math.radians(0)
				elif event.key == pygame.K_DOWN:
					turretMove = math.radians(0)
				elif event.key == pygame.K_SEMICOLON:
					powerChange = 0
				elif event.key == pygame.K_SLASH:
					powerChange = 0
				if event.key == pygame.K_a:
					enemyTankMove = 0
				elif event.key == pygame.K_d:
					enemyTankMove = 0
				elif event.key == pygame.K_w:
					enemyTurretMove = math.radians(0)
				elif event.key == pygame.K_s:
					enemyTurretMove = math.radians(0)
				#elif event.key == pygame.K_SPACE:
				#	action = "stop"
		
		mainTankX += tankMove
		enemyTankX += enemyTankMove
		
		turretAngle += turretMove
		enemyTurretAngle += enemyTurretMove
		
		#fill the background with a colors
		gameDisplay.fill(white)
		
		#draw health bars
		display_health_bars(player_health,enemy_health)
		
		#draw barrier
		display_barrier(xlocation,randomHeight,barrierWidth)
		
		#draw ground
		gameDisplay.fill(green,rect=[0,display_height-groundHeight,display_width,groundHeight])
		
		#add restriction to the movement of main tank turret
		if math.degrees(turretAngle)>=90:	#if turretAngle is greater than 90 degree then stop moving it further
			turretAngle = math.radians(89)	#not 90 bcoz then laser will be parallel to y-axis therefore it won't intersect y-axis hence shoot_laser function will give error
		elif math.degrees(turretAngle)<0:
			turretAngle = math.radians(0)
			
		#add restriction to the movement of enemy tank turret
		if math.degrees(enemyTurretAngle)>=90:	#if turretAngle is greater than 90 degree then stop moving it further
			enemyTurretAngle = math.radians(89)	#not 90 bcoz then laser will be parallel to y-axis therefore it won't intersect y-axis hence shoot_laser function will give error
		elif math.degrees(enemyTurretAngle)<0:
			enemyTurretAngle = math.radians(0)
		
		#add restriction to the movement of the main tank so that it does not cross the screen boundaries
		if mainTankX + tankWidth >= display_width:	#restriction for right screen boundary
			mainTankX = display_width - tankWidth
		elif mainTankX - tankWidth <= xlocation + barrierWidth:	#restriction for right barrier boundary
			mainTankX = xlocation + barrierWidth + tankWidth
			
		#add restriction to the movement of the enemy tank so that it does not cross the screen boundaries
		if enemyTankX - tankWidth <= 0:	#restriction for left screen boundary
			enemyTankX = tankWidth
		elif enemyTankX + tankWidth >= xlocation:	#restriction for left barrier boundary
			enemyTankX = xlocation - tankWidth
		
		# display tank
		display_tank(mainTankX,mainTankY,turretAngle)
		
		#display enemy tank
		display_enemyTank(enemyTankX,enemyTankY)
		
		#display power level
		power += powerChange
		display_power(power)
		
		display_score(score)
		pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set
		
		clock.tick(FPS)	#defines 10 frames per second

	pygame.quit()	#it de-initialises the pygame

	quit() 
	
game_intro()