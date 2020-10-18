import pygame, numpy, os
from states.StateHandler import StateHandler
from lib.SpriteHandler import SpriteHandler
from lib.MineTile import MineTile
from lib.Buttons import Buttons

class MineField:
	def __init__(mf,screen,width,height,mine_count,coordinates=(0,0),scaleRatio=2):
		# CLASS VARIABLES
		mf.coordinates = coordinates
		mf.scaleRatio = scaleRatio
		mf.screen = screen
		mf.width = width
		mf.height = height
		mf.tile_padding = 0

		# UNIQUE CLASS VARIABLES
		mf.mine_count = mine_count
		mf.mine_triggered = False
		mf.list = [[0 for x in range(width)] for y in range(height)]
		mf.board = []
		mf.bomb_coords = []
		mf.revealed_tiles = []
		mf.covered_count = 0

		mf.generate()

	# RETURNS TRUE IF THE GAME HAS BEEN WON
	def gameWon(mf):
		for y in range(len(mf.board)):
			for x in range(len(mf.board[y])):
				if mf.board[y][x].isCovered():
					mf.covered_count+=1
		game_won = mf.covered_count == mf.mine_count
		mf.covered_count = 0
		return game_won

	# RETURNS THE NUMBER OF CORRECT FLAGS
	def getCorrectFlags(mf):
		correct_flags = 0
		for y in range(len(mf.board)):
			for x in range(len(mf.board[y])):
				if "Flag" in mf.board[y][x].state and mf.list[y][x] == -1:
					correct_flags += 1
		return correct_flags

	# RETURNS THE NUMBER OF REVEALED SPACES
	def getSpaces(mf):
		revealed = 0
		for y in range(len(mf.board)):
			for x in range(len(mf.board[y])):
				if mf.board[y][x].isRevealed():
					revealed+=1
		return revealed

	# SETS THE COORDINATES OF THE BOARD
	def setCoord(mf,coordinates):
		mf.coordinates = coordinates

	# GENERATES THE MINE FIELD
	def generate(mf):
		while(len(mf.bomb_coords) < mf.mine_count):
			for y in range(mf.height):
				for x in range(mf.width):
					if len(mf.bomb_coords) == mf.mine_count:
						break
					else:
						chance = 1/(mf.width*mf.height)
						isMine = numpy.random.choice([True,False],p=[chance,1-chance])
						if isMine and [y,x] not in mf.bomb_coords:
							mf.bomb_coords.append([y,x])
							mf.list[y][x] = -1

							row_range = range(y-1,y+2)
							col_range = range(x-1,x+2)

							for i in row_range:
								for j in col_range:
									if(0<=i<mf.height and 0<=j<mf.width and mf.list[i][j] != -1):
										mf.list[i][j] += 1	
		# MAKE TILES
		for y in range(mf.height):
			mf.board.append([])
			for x in range(mf.width):
				mf.board[y].append(MineTile(mf.screen,(x,y),scaleRatio=mf.scaleRatio,board_list=mf.list))

	# SHOWS ALL MINES
	def showAllMines(mf):
		for y in range(len(mf.board)):
			for x in range(len(mf.board[y])):
				if mf.list[y][x] == -1 and "Mine" not in mf.board[y][x].state:
					try:
						mf.board[y][x].state.remove("Tile")
					except:
						pass
					mf.board[y][x].state.append("Tile_active")
					mf.board[y][x].state.append("Mine")

	# REVEALS THE CONTIGUOUS CELL BLOCKS WHEN AN EMPTY CELL IS REVEALED
	def revealContiguousBlocks(mf,coordinates):
		row,col = coordinates
		mf.revealed_tiles.append((row,col))

		row_range = range(row-1,row+2)
		col_range = range(col-1,col+2)

		if mf.list[row][col] == 0:
			for y in row_range:
				for x in col_range:
					withinBounds = (0<=y<mf.height and 0<=x<mf.width)
					if withinBounds and mf.list[y][x] != -1:
						if "Tile_active" not in mf.board[y][x].state:
							try:
								mf.board[y][x].state.remove("Tile")
								mf.board[y][x].state.remove("Flag")
							except:
								pass
							mf.board[y][x].state.append("Tile_active")
							if mf.list[y][x] == -1:
								mf.board[y][x].state.append("Mine")
							elif mf.list[y][x] == 1:
								mf.board[y][x].state.append("1")
							elif mf.list[y][x] == 2:
								mf.board[y][x].state.append("2")
							elif mf.list[y][x] == 3:
								mf.board[y][x].state.append("3")
							elif mf.list[y][x] == 4:
								mf.board[y][x].state.append("4")
							elif mf.list[y][x] == 5:
								mf.board[y][x].state.append("5")
							elif mf.list[y][x] == 6:
								mf.board[y][x].state.append("6")
							elif mf.list[y][x] == 7:
								mf.board[y][x].state.append("7")
							elif mf.list[y][x] == 8:
								mf.board[y][x].state.append("8")
		return "Tile_active"

	# SETS THE FIELD'S RELATIVE COORDINATE
	def setRelCoord(mf,relcoordinates):
		w, h = pygame.display.get_surface().get_size()
		sw = mf.width*(mf.board[0][0].width+mf.tile_padding)
		sh = mf.height*(mf.board[0][0].height+mf.tile_padding)
		mf.coordinates = ((w*(relcoordinates[0]/100))-(sw/2),(h*(relcoordinates[1]/100))-(sh/2))

	# RENDERS THE MINE FIELD
	def render(mf):
		for y in range(len(mf.board)):
			for x in range(len(mf.board[y])):
				# UPDATE
				if mf.mine_triggered == False:
					mf.board[y][x].update()
				if mf.board[y][x].isRevealed() and (y,x) not in mf.revealed_tiles:
					if mf.list[y][x] == 0:
						mf.board[y][x].state.append(mf.revealContiguousBlocks((y,x)))
				if mf.board[y][x].isRevealed() and "Mine" in mf.board[y][x].state:
					mf.mine_triggered = True

				# RENDER
				x_offset = mf.board[0][0].width+mf.tile_padding
				y_offset = mf.board[0][0].height+mf.tile_padding
				mf.board[y][x].x = x*x_offset+mf.coordinates[0]
				mf.board[y][x].y = y*y_offset+mf.coordinates[1]
				for i in range(len(mf.board[y][x].state)):
					mf.board[y][x].render()



