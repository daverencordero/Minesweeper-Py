#!/usr/bin/python3

# CONFIG IMPORTS
from lib.Config import Config
config = Config()

# MISC IMPORTS
import os, platform, random
import keyboard, pygame,numpy

# LIB IMPORTS
from lib.Swatches import Swatches
from lib.Background import Background

# STATE IMPORTS
from states.StateHandler import StateHandler
from states.MenuState import MenuState
from states.GameState import GameState
from states.NewGameState import NewGameState
from states.HighScoreState import HighScoreState

"""
==========
GAME SETUP
==========
"""

# GLOBAL VARIABLES
display_width = int(config.items["window_width"])
dispay_height = int(config.items["window_height"])

# PYGAME SWATCHES
swatches = Swatches()
swatches.add(0,"#00A3BF")
swatches.add(1,"#EBB000")
swatches.add(2,"#007C91")
swatches.add(3,"#003640")
swatches.add(4,"#EF5900")

# PYGAME INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((display_width,dispay_height))
pygame.display.set_caption('Minesweeper')
clock = pygame.time.Clock()

# MENU INITIALIZATION
bg = Background(screen,"BG")
menu = MenuState(screen,swatches,bg)
newGame = NewGameState(screen,swatches,bg)
game = GameState(screen,swatches,bg)
highScore = HighScoreState(screen,swatches,bg)
StateHandler.addState("menu",menu)
StateHandler.addState("new_game",newGame)
StateHandler.addState("game",game)
StateHandler.addState("high_score",highScore)
StateHandler.setState("menu")

"""
==========
GAME LOOP
==========
"""
isRunning = True
while(isRunning):
	# CATCHES PYGAME EXIT
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
	
	# MAIN LOOP
	if(StateHandler.getCurrentState()!=None):
		StateHandler.getCurrentState().render()

	# SCREEN UPDATES
	pygame.display.update()
	clock.tick(60)

pygame.quit()