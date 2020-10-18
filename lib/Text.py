import pygame,os

class Text:
	def __init__(txt,screen,label,coordinates=(0,0)):
		# CLASS VARIABLES
		txt.screen = screen
		txt.x, txt.y = coordinates
		txt.font = pygame.font.Font(os.getcwd()+"\\res\\Roboto-Bold.ttf", 30)
		txt.label = label
		txt.text = txt.font.render(label,1, (255,255,255))
	
	# SETS TEXT RELATIVE COORDINATES
	def setRelCoord(txt,relcoordinates):
		text_width, text_height = txt.font.size(txt.label)
		w, h = pygame.display.get_surface().get_size()
		coordinates = ((w*(relcoordinates[0]/100))-(text_width/2),(h*(relcoordinates[1]/100))-(text_height/2))
		txt.x, txt.y = coordinates
	
	# RENDERS TEXT
	def render(txt):
		txt.screen.blit(txt.text,(txt.x,txt.y))