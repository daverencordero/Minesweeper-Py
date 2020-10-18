import pygame

class Buttons:
	def __init__(btn,sprite):
		btn.sprite = sprite

	# CHECK IF A BUTTON IS CLICKED
	def isPressed(btn):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		x,y = btn.sprite[1]
		w,h = btn.sprite[2]
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			if click[0] == 1:
				return True
		return False

	# CHECKS IF A BUTTON IS RIGHT CLICKED
	def isRightPressed(btn):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		x,y = btn.sprite[1]
		w,h = btn.sprite[2]
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			if click[2] == 1:
				return True
		return False