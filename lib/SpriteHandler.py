import pygame, os

class SpriteHandler:
	def __init__(spr,screen):
		spr.screen = screen
		spr.screen_dim = pygame.display.get_surface().get_size()
		spr.list = {}
		spr.scale_ratio = 1

	# ADD FUNCTIONS
	def addMultiple(spr, sprite_names, coordinates=(0,0)):
		for name in sprite_names:
			try:
				spr.list[name]=[pygame.image.load(os.getcwd()+'\\res\\'+name+'.png'),coordinates]
				sw, sh = spr.list[name][0].get_rect().size
				spr.list[name].append((sw,sh))
			except:
				print("SpriteHandler: '%s'.png is not found" %name)	

	def add(spr,sprite_name,coordinates=(0,0)):
		try:
			spr.list[sprite_name]=[pygame.image.load(os.getcwd()+'\\res\\'+sprite_name+'.png'),coordinates]
			sw, sh = spr.list[sprite_name][0].get_rect().size
			spr.list[sprite_name].append((sw,sh))
		except:
			print("SpriteHandler: '%s'.png is not found" %sprite_name)

	# COORDINATE FUNCTIONS
	def setAllCoord(spr,coordinates,exclusions=[]):
		for key,value in spr.list.items():
			if key in exclusions:
				continue
			spr.list[key][1] = coordinates

	def setCoord(spr,name,coordinates):
		spr.list[name][1] = coordinates

	def setRelCoord(spr,name,relcoordinates):
		w, h = pygame.display.get_surface().get_size()
		sw, sh = spr.list[name][0].get_rect().size
		spr.list[name][1] = ((w*(relcoordinates[0]/100))-(sw/2),(h*(relcoordinates[1]/100))-(sh/2))

	def setRowRelCoord(spr,names,relcoordinates,distance=10):
		length = len(names)
		if length%2 == 1:
			for index in range(length):
				spr.setRelCoord(names[index],(relcoordinates[0]-((1/length)*(distance*length))+(index*distance),relcoordinates[1]))
		if length%2 == 0:
			for index in range(length):
				spr.setRelCoord(names[index],(relcoordinates[0]-((1/length)*(distance*length))+(distance/2)+(index*distance),relcoordinates[1]))


	# SCALE FUNCTIONS
	def setScaleRatio(spr,percentage,basis_name):
		value = int((percentage/100)*spr.screen_dim[0])
		spr.scale_ratio = value/spr.list[basis_name][2][0]

	def scale(spr,name, scale):
		spr.list[name][2] = scale

	def scaleAllToScreen(spr,exclusions=[]):
		for key,value in spr.list.items():
			if key in exclusions:
				continue
			spr.list[key][2] = (int(spr.list[key][2][0]*spr.scale_ratio),int(spr.list[key][2][1]*spr.scale_ratio))

	def scaleToScreen(spr,name):
		spr.list[name][2] = (int(spr.list[key][2][0]*spr.scale_ratio),int(spr.list[key][2][1]*spr.scale_ratio))


	# RENDER FUNCTIONS
	def renderAll(spr,exclusions=[]):
		for key,value in spr.list.items():
			if key in exclusions:
				continue
			spr.list[key][0] = pygame.transform.scale(spr.list[key][0],spr.list[key][2])
			spr.screen.blit(spr.list[key][0], value[1])

	def render(spr,name):
		try:
			spr.list[name][0] = pygame.transform.scale(spr.list[name][0],spr.list[name][2])
			spr.screen.blit(spr.list[name][0], spr.list[name][1])
		except:
			print("SpriteHandler: '%s' name is not in the list" %name)
