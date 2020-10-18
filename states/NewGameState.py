import pygame
from states.StateHandler import StateHandler
from lib.SpriteHandler import SpriteHandler
from lib.Buttons import Buttons

class NewGameState(StateHandler):
	def __init__(ngm,screen,swatches,background):
		# STATE CLASS INIT
		ngm.screen = screen
		ngm.swatches = swatches
		ngm.background = background
		ngm.active_game_mode = None
		ngm.game_mode = None
		
		# SPRITES INIT
		ngm.sprites = SpriteHandler(screen)
		ngm.sprite_names = ["8x8_active","16x16_active","16x30_active","8x8","16x16","16x30","Play_Button_02","Load_Game"]
		ngm.sprites.addMultiple(ngm.sprite_names)
		ngm.sprites.setScaleRatio(25,"8x8")
		ngm.sprites.scaleAllToScreen()



	def render(ngm):
		ngm.screen.fill(ngm.swatches.list[3])
		ngm.background.render()

		# SETTING MENU SPRITES LOCATIONS
		ngm.sprites.setRowRelCoord(["8x8_active","16x16_active","16x30_active"],(50,50),25)
		ngm.sprites.setRowRelCoord(["8x8","16x16","16x30"],(50,50),25)
		ngm.sprites.setRelCoord("Play_Button_02",(80,80))
		ngm.sprites.setRelCoord("Load_Game",(20,80))

		# MAKING BUTTONS
		_8x8_btn = Buttons(ngm.sprites.list["8x8"])
		_16x16_btn = Buttons(ngm.sprites.list["16x16"])
		_16x30_btn = Buttons(ngm.sprites.list["16x30"])
		load_btn = Buttons(ngm.sprites.list["Load_Game"])
		play_btn = Buttons(ngm.sprites.list["Play_Button_02"])

		ngm.sprites.renderAll([ngm.active_game_mode])

		# SETS THE PARAMETERS AND INITIALIZES GAME STATEs
		if ngm.game_mode != None and play_btn.isPressed():
			StateHandler.getState("game").setParameters(ngm.game_mode)
			StateHandler.setState("game")
		elif load_btn.isPressed():
			StateHandler.getState("game").setParameters("load_game")
			StateHandler.setState("game")
		else:
			if _8x8_btn.isPressed():
				ngm.active_game_mode = "8x8"
				ngm.game_mode = "8x8"
			if _16x16_btn.isPressed():
				ngm.active_game_mode = "16x16"
				ngm.game_mode = "16x16"
			if _16x30_btn.isPressed():
				ngm.active_game_mode = "16x30"
				ngm.game_mode = "16x30"