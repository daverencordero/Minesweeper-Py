import pygame
from states.StateHandler import StateHandler
from lib.SpriteHandler import SpriteHandler
from lib.Buttons import Buttons

class MenuState(StateHandler):
	def __init__(menu,screen,swatches,background):
		# STATE CLASS INIT
		menu.options = ["New Game","Load Game","Options","Star"]
		menu.screen = screen
		menu.swatches = swatches
		menu.background = background

		# SPRITES INIT
		menu.sprites = SpriteHandler(screen)
		menu.sprite_names = ["Title","Play_Button","Star","Settings"]
		menu.sprites.addMultiple(menu.sprite_names)
		menu.sprites.setScaleRatio(75,"Title")
		menu.sprites.scaleAllToScreen()

	def render(menu):
		# RENDERING BACKGROUND
		menu.screen.fill(menu.swatches.list[3])
		menu.background.render()

		# SETTING MENU SPRITES LOCATIONS
		menu.sprites.setRelCoord("Title",(50,40))
		menu.sprites.setRowRelCoord(["Star","Play_Button","Settings"],(50,65),10)

		# MAKING BUTTONS
		play_btn = Buttons(menu.sprites.list["Play_Button"])
		settings_btn = Buttons(menu.sprites.list["Settings"])
		star_btn = Buttons(menu.sprites.list["Star"])

		menu.sprites.render("Title")
		menu.sprites.render("Star")
		menu.sprites.render("Play_Button")

		# UPDATING BUTTONS
		if play_btn.isPressed():
			StateHandler.setState("new_game")
		if star_btn.isPressed():
			StateHandler.setState("high_score")