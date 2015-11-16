# setting pixels on screen
import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(green)

Pixel = pygame.PixelArray(gameDisplay)	#set the whole screen as pixel array
Pixel[10][10] = black	# setting (10,10) pixel as black
Pixel[10][11] = black
Pixel[10][12] = black
Pixel[10][13] = black

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	pygame.display.update()