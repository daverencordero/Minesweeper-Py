import pygame,os
from states.StateHandler import StateHandler
from lib.SpriteHandler import SpriteHandler
from lib.Buttons import Buttons
from lib.MineField import MineField
from lib.Text import Text

class GameState:
	def __init__(gm,screen,swatches,background):
		# STATE CLASS INIT
		gm.screen = screen
		gm.swatches = swatches
		gm.background = background
		gm.clock = pygame.time.Clock()
		gm.minutes = 0
		gm.seconds = 0
		gm.milliseconds = 0
		gm.total_score = 0
		gm.isHighScore = False
		gm.highscore_list = None
		gm.game_mode = None
		gm.field = None

		# SPRITES INIT
		gm.sprites = SpriteHandler(screen)
		gm.sprite_names = ["Restart","Save","Timer","Mine_Count","Game_Over","Play_Button","Exit_02","You_Win","High_Scores","Home"]
		gm.sprites.addMultiple(gm.sprite_names)
		gm.sprites.setScaleRatio(8,"Restart")
		gm.sprites.scaleAllToScreen()
	
	# SETS THE PARAMETERS OF THE GAME AND GENERATES MINEFIELD
	def setParameters(gm, game_mode="8x8"):
		gm.game_mode = game_mode
		if(gm.game_mode =="8x8"):
			gm.field = MineField(gm.screen,8,8,10,scaleRatio=4)
		elif(gm.game_mode == "16x16"):
			gm.field = MineField(gm.screen,16,16,40,scaleRatio=2.5)
		elif(gm.game_mode == "16x30"):
			gm.field = MineField(gm.screen,30,16,99,scaleRatio=2.5)
		elif(gm.game_mode == "load_game"):
			gm.loadGame()

	# GETS THE LOAD DATA FROM THE SAVE FILE
	def loadGame(gm):
		save_file = open("save_file.txt","r")
		game_list = []
		for index,line in enumerate(save_file):
			popped_line = line.split(",")
			popped_line.pop()
			game_list.append(popped_line)
		save_file.close()

		if (len(game_list) == 8):
			gm.field = MineField(gm.screen,8,8,10,scaleRatio=4)
			gm.game_mode = "8x8"
		elif (len(game_list[0]) == 16):
			gm.field = MineField(gm.screen,16,16,40,scaleRatio=2.5)
			gm.game_mode = "16x16"
		elif (len(game_list[0]) == 30):
			gm.field = MineField(gm.screen,30,16,99,scaleRatio=2.5)
			gm.game_mode = "16x30"

		for y in range(len(game_list)):
			for x in range(len(game_list[y])):
				game_list[y][x] = int(game_list[y][x])


		gm.field.list = game_list

		for y in range(len(game_list)):
			for x in range(len(game_list[y])):
				gm.field.board[y][x].list = game_list

		state_list = []	
		save_file_2 = open("save_file_2.txt","r")
		for index,line in enumerate(save_file_2):
			popped_line = line.split(",")
			popped_line.pop()
			state_list.append(popped_line)
		save_file_2.close()

		for y in range(len(state_list)):
			for x in range(len(state_list[y])):
				if state_list[y][x] == "1":
					try:
						gm.field.board[y][x].state.remove("Tile")
						gm.field.board[y][x].state.remove("Flag")
					except:
						pass
					gm.field.board[y][x].state.append("Tile_active")
					if gm.field.list[y][x] == 1:
						gm.field.board[y][x].state.append("1")
					elif gm.field.list[y][x] == 2:
						gm.field.board[y][x].state.append("2")
					elif gm.field.list[y][x] == 3:
						gm.field.board[y][x].state.append("3")
					elif gm.field.list[y][x] == 4:
						gm.field.board[y][x].state.append("4")
					elif gm.field.list[y][x] == 5:
						gm.field.board[y][x].state.append("5")
					elif gm.field.list[y][x] == 6:
						gm.field.board[y][x].state.append("6")
					elif gm.field.list[y][x] == 7:
						gm.field.board[y][x].state.append("7")
					elif gm.field.list[y][x] == 8:
						gm.field.board[y][x].state.append("8")
				elif state_list[y][x] == "F":
					gm.field.board[y][x].state.append("Flag")
				elif state_list[y][x] == "0":
					pass

	# CREATES A SAVE FILE AND SAVES CURRENT GAME STATE
	def saveGame(gm):
		save_file = open("save_file.txt","w")
		for y in gm.field.list:
			for x in y:
				save_file.write(str(x)+",")
			save_file.write("\n")
		save_file.close()

		save_file_2 = open("save_file_2.txt","w")
		for y in gm.field.board:
			for x in y:
				if "Tile_active" in x.state:
					save_file_2.write("1"+",") 
				elif "Flag" in x.state:
					save_file_2.write("F"+",")
				else:
					save_file_2.write("0"+",")
			save_file_2.write("\n")
		save_file_2.close()

	# CHECKS IF THE TOTAL SCORE IS THE HIGH SCORE
	def checkHighScore(gm,time,correct_flags,revealed_cells,totalscore):
		parameters = []
		highscore = 0

		try:
			highscore_file = open("highscore.txt","r")
			for index,line in enumerate(highscore_file):
				parameters = line.split(',')
			highscore_file.close()

			if totalscore > int(parameters[0]):
				gm.isHighScore = True
				highscore_file = open("highscore.txt","w")
				print("{},{},{},{}".format(totalscore,revealed_cells,correct_flags,time))
				highscore_file.write("{},{},{},{}".format(totalscore,revealed_cells,correct_flags,time))
				highscore_file.close()
		except:
			highscore_file = open("highscore.txt","w")
			highscore_file.write("0,0,0,0")
			highscore_file.close()
		
		return parameters[3],parameters[2],parameters[1],parameters[0]

	# FACILITATES THE STOPWATCH FOUND IN THE GAME
	def stopwatch(gm):
		if(not gm.field.mine_triggered and not gm.field.gameWon()):
			if gm.milliseconds > 1000:
				gm.seconds += 1
				gm.milliseconds -= 1000
			if gm.seconds > 60:
				gm.minutes += 1
				gm.seconds -= 60
			gm.milliseconds += gm.clock.tick_busy_loop(60)
	
	def render(gm):
		# RENDERS BACKGROUND
		gm.screen.fill(gm.swatches.list[3])
		gm.background.render()

		# SETS THE RELATIVE COORDINATES OF THE FIELD AND RENDERS IT
		if(gm.game_mode =="8x8"):
			gm.field.setRelCoord((50,50))
		elif(gm.game_mode == "16x16"):
			gm.field.setRelCoord((50,58))
		elif(gm.game_mode == "16x30"):
			gm.field.setRelCoord((50,58))
		gm.field.render()

		# INITIALIZES THE BUTTONS
		gm.sprites.setRowRelCoord(["Home","Save"],(50,88),85)
		gm.sprites.setRowRelCoord(["Restart","Play_Button"],(50,65),35)
		gm.sprites.setRelCoord("Timer",(50,10))
		gm.sprites.setRelCoord("Game_Over",(50,50))
		gm.sprites.setRelCoord("You_Win",(50,50))
		gm.sprites.setRelCoord("High_Scores",(50,50))
		gm.sprites.render("Timer")
		gm.sprites.render("Home")
		gm.sprites.render("Save")

		gm.stopwatch()

		# MAKING BUTTONS
		home = Buttons(gm.sprites.list["Home"])
		save = Buttons(gm.sprites.list["Save"])

		# TEXT RENDERING
		try:
			gm.total_score = int((gm.field.getSpaces()/gm.seconds)*1000+(gm.field.getCorrectFlags()/gm.seconds)*1000)
		except:
			gm.total_score = 0

		gm.timelabel = Text(gm.screen,"{}:{}:{}".format(gm.minutes, gm.seconds,gm.milliseconds))
		gm.timescore = Text(gm.screen,"Time: {}:{}:{}".format(gm.minutes, gm.seconds,gm.milliseconds))
		gm.flagscore = Text(gm.screen,"Correct Flags: {}".format(gm.field.getCorrectFlags()))
		gm.cellscore = Text(gm.screen,"Revealed Cells: {}".format(gm.field.getSpaces()))
		gm.totalscore = Text(gm.screen,"Total: {}".format(gm.total_score))
		gm.highscore = Text(gm.screen,"Highscore: {}".format(gm.total_score))
		gm.timelabel.setRelCoord((50,10))
		gm.timescore.setRelCoord((50,40))
		gm.flagscore.setRelCoord((50,45))
		gm.cellscore.setRelCoord((50,50))
		gm.highscore.setRelCoord((50,58))
		gm.totalscore.setRelCoord((50,58))
		gm.timelabel.render()

		# UPDATES BURRONS
		if home.isPressed():
			StateHandler.setState("menu")

		elif save.isPressed():
			gm.saveGame()

		# CHECKS IF A MINE IS TRIGGERED TO RENDER THE GAME OVER SCREEN
		if gm.field.mine_triggered:
			gm.field.showAllMines()
			gm.field.render()
			gm.sprites.render("Game_Over")
			gm.sprites.render("Restart")
			gm.sprites.render("Play_Button")
			gm.totalscore.render()
			gm.timescore.render()
			gm.flagscore.render()
			gm.cellscore.render()

			restart = Buttons(gm.sprites.list["Restart"])
			play = Buttons(gm.sprites.list["Play_Button"])

			if restart.isPressed():
				gm.setParameters(gm.game_mode)
				gm.minutes = 0
				gm.seconds = 0
				gm.milliseconds = 0
				gm.field.mine_triggered = False

			if play.isPressed():
				StateHandler.setState("new_game")	

		# CHECKS IF THE GAME IS WON TO RENDER GAME WON SCREEN
		elif gm.field.gameWon():
			time_val = "{}:{}:{}".format(gm.minutes, gm.seconds,gm.milliseconds)
			correct_flags_val = gm.field.getCorrectFlags()
			revealed_cells_val = gm.field.getSpaces()
			total_score_val = gm.total_score
			gm.highscore_list = gm.checkHighScore(time_val,correct_flags_val,revealed_cells_val,total_score_val)

			# CHECKS IF THE SCORE IS A HIGH SCORE TO RENDER THE HIGH SCORE SCREEN
			if (gm.isHighScore):
				gm.sprites.render("High_Scores")
				gm.sprites.render("Restart")
				gm.sprites.render("Play_Button")
				gm.highscore.render()
				gm.timescore.render()
				gm.flagscore.render()
				gm.cellscore.render()
				
				restart = Buttons(gm.sprites.list["Restart"])
				play = Buttons(gm.sprites.list["Play_Button"])
				
				if restart.isPressed():
					gm.setParameters(gm.game_mode)
					gm.minutes = 0
					gm.seconds = 0
					gm.milliseconds = 0
					gm.field.mine_triggered = False
				if play.isPressed():
					StateHandler.setState("new_game")

			# SIMPLY RENDERS THE GAME WON SCREEN
			else:
				gm.sprites.render("You_Win")
				gm.sprites.render("Restart")
				gm.sprites.render("Play_Button")
				gm.totalscore.render()
				gm.timescore.render()
				gm.flagscore.render()
				gm.cellscore.render()
				
				restart = Buttons(gm.sprites.list["Restart"])
				play = Buttons(gm.sprites.list["Play_Button"])
				
				if restart.isPressed():
					gm.setParameters(gm.game_mode)
					gm.minutes = 0
					gm.seconds = 0
					gm.milliseconds = 0
					gm.field.mine_triggered = False
				if play.isPressed():
					StateHandler.setState("new_game")	
			
