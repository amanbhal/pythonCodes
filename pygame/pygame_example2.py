# drawing stuff
import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(green)

#drawing line
pygame.draw.line(gameDisplay,red,(100,100),(300,300))	# starting point // ending point

#drawing circle
pygame.draw.circle(gameDisplay,black,(400,400),50) 	# center // radius

#drawing rectangle
pygame.draw.rect(gameDisplay,white,(300,300,50,50)) #top left point,width,height

#drawing polygon. Polygon is drawn based on the order of the points given as arguments
pygame.draw.polygon(gameDisplay,blue,((10,10),(40,40),(70,17),(90,35)))	#vertex points

Pixel = pygame.PixelArray(gameDisplay)	#set the whole screen as pixel array
Pixel[10][10] = black	# setting (10,10) pixel as black

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	pygame.display.update()