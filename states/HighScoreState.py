import pygame
from states.StateHandler import StateHandler
from lib.SpriteHandler import SpriteHandler
from lib.Buttons import Buttons
from lib.Text import Text

class HighScoreState:
	def __init__(hss,screen,swatches,background):
		# STATE CLASS INIT
		hss.screen = screen
		hss.swatches = swatches
		hss.background = background
		hss.time = ""
		hss.correct_flags = 0
		hss.revealed_cells = 0
		hss.totalscore = 0

		# SPRITES INIT
		hss.sprites = SpriteHandler(screen)
		hss.sprite_names = ["Restart","High_Scores","Home"]
		hss.sprites.addMultiple(hss.sprite_names)
		hss.sprites.setScaleRatio(8,"Restart")
		hss.sprites.scaleAllToScreen()

	# CHECKS IF THE OBTAINED SCORE IS THE HIGHEST SCORE
	def checkHighScore(hss):
		parameters = []
		highscore = 0
		try:
			highscore_file = open("highscore.txt","r")
			for index,line in enumerate(highscore_file):
				parameters = line.split(',')
			highscore_file.close()

			hss.time = parameters[3]
			hss.correct_flags = int(parameters[2])
			hss.revealed_cells = int(parameters[1])
			hss.totalscore = int(parameters[0])
		except:
			return None

	def render(hss):
		# RENDERING BACKGROUND
		hss.screen.fill(hss.swatches.list[3])
		hss.background.render()

		# SETTING MENU SPRITES LOCATIONS
		hss.sprites.setRelCoord("High_Scores",(50,50))
		hss.sprites.setRelCoord("Home",(50,88))
		hss.sprites.render("High_Scores")
		hss.sprites.render("Home")
		
		hss.checkHighScore()

		# INITIALIZING TEXT
		hss.nohighscore = Text(hss.screen,"There is no Highscore!")
		hss.timescore = Text(hss.screen,"Time: {}".format(hss.time))
		hss.flagscore = Text(hss.screen,"Correct Flags: {}".format(hss.correct_flags))
		hss.cellscore = Text(hss.screen,"Revealed Cells: {}".format(hss.revealed_cells))
		hss.highscore = Text(hss.screen,"Highscore: {}".format(hss.totalscore))
		hss.nohighscore.setRelCoord((50,50))
		hss.timescore.setRelCoord((50,40))
		hss.flagscore.setRelCoord((50,45))
		hss.cellscore.setRelCoord((50,50))
		hss.highscore.setRelCoord((50,58))

		# RENDERING TEXT
		if hss.totalscore == None:
			hss.nohighscore.render()
		else:
			hss.timescore.render()
			hss.flagscore.render()
			hss.cellscore.render()
			hss.highscore.render()

		# MAKING AND UPDATING BUTTONS
		home = Buttons(hss.sprites.list["Home"])
		if home.isPressed():
			StateHandler.setState("menu")