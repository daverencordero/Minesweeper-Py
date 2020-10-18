class Swatches:
	def __init__(sw):
		sw.list = {}

	# ADDS A SWATCH
	def add(sw,name,hex):
		sw.list[name]=sw.hex_to_rgb(hex)

	# REMOVE A SWATCH
	def remove(sw,name):
		del sw.list[name]

	# CONVERTS HEX VALUE TO RGB
	def hex_to_rgb(sw,value):
	    value = value.lstrip('#')
	    lv = len(value)
	    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))