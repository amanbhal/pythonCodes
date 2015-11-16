import pygame

x = pygame.init()	#it initialises the pygame

gameDisplay = pygame.display.set_mode((800,600))	#it builds a canvas/screen to run the game

pygame.display.update()	#it updates the whole screen. it can update a specific area if arguments are set

pygame.quit()	#it de-initialises the pygame

quit() 