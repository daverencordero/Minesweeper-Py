from lib.SpriteHandler import SpriteHandler
import pygame

class Background:
	def __init__(bg,screen,name):
		bg.screen = screen
		bg.screen_dim = pygame.display.get_surface().get_size()
		bg.sprite = SpriteHandler(screen)
		bg.sprite.add(name)

	# GETS AND RENDERS BACKGROUND
	def render(bg):
		bg.sprite.scale("BG",(bg.screen_dim[0],bg.screen_dim[1]))
		bg.sprite.renderAll()