import pygame, numpy
from states.StateHandler import StateHandler
from lib.SpriteHandler import SpriteHandler
from lib.Buttons import Buttons

class MineTile:
	def __init__(mt,screen,board_coordinates,coordinates=(0,0),scaleRatio=2,board_list=[[]]):
		# CLASS VARIABLES
		mt.bx,mt.by = board_coordinates
		mt.x, mt.y = coordinates
		mt.height = None
		mt.width = None
		mt.screen = screen
		mt.scaleRatio = scaleRatio
		mt.buttons = {}
		mt.list = board_list
		mt.sprites = None
		mt.state = ["Tile"]

		# SPRITES INIT
		mt.sprites = SpriteHandler(mt.screen)
		mt.sprite_names = ["Tile_active","1","2","3","4","5","8","Flag","Mine","Tile"]
		mt.sprites.addMultiple(mt.sprite_names)
		mt.sprites.setScaleRatio(mt.scaleRatio,"Tile_active")
		mt.sprites.scaleAllToScreen()
		mt.width,mt.height = mt.sprites.list["1"][2]

		# BUTTONS INIT
		for name in mt.sprite_names:
			mt.buttons[name] = Buttons(mt.sprites.list[name])

	# CHECKS IF TILE IS NOT YET REVEALED
	def isCovered(mt):
		return ("Tile" in mt.state)

	# CHECKS IF TILE IS REVEALED
	def isRevealed(mt):
		return ("Tile_active" in mt.state)

	# UPDATES IF TILE IS CLICKED TO REVEAL IT
	def update(mt):
		if not mt.isRevealed():
			if mt.buttons["Tile"].isRightPressed():
				if "Flag" in mt.state: 
					mt.state.remove("Flag")
				else:
					mt.state.append("Flag")

			if mt.buttons["Tile"].isPressed() or mt.isRevealed():
				try:
					mt.state.remove("Tile")
					mt.state.remove("Flag")
				except:
					pass
				if mt.list[mt.by][mt.bx] != 0:
					mt.state.append("Tile_active")
				if mt.list[mt.by][mt.bx] == -1:
					mt.state.append("Mine")
				elif mt.list[mt.by][mt.bx] == 1:
					mt.state.append("1")
				elif mt.list[mt.by][mt.bx] == 2:
					mt.state.append("2")
				elif mt.list[mt.by][mt.bx] == 3:
					mt.state.append("3")
				elif mt.list[mt.by][mt.bx] == 4:
					mt.state.append("4")
				elif mt.list[mt.by][mt.bx] == 5:
					mt.state.append("5")
				elif mt.list[mt.by][mt.bx] == 6:
					mt.state.append("6")
				elif mt.list[mt.by][mt.bx] == 7:
					mt.state.append("7")
				elif mt.list[mt.by][mt.bx] == 8:
					mt.state.append("8")
				elif mt.list[mt.by][mt.bx] == 0:
					mt.state.append("Tile_active")
	
	# RENDERS TILE
	def render(mt):
		for name in range(len(mt.state)):
			mt.sprites.setAllCoord((mt.x,mt.y))
			mt.sprites.render(mt.state[name])