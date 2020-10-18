import os
import socket

class Config:
	def __init__(cfg):
		cfg.items = {}
		cfg.get()
		cfg.installCR()

	# INSTALLS COMMON REDISTRIBUTION
	def installCR(cfg):
		if cfg.items["first_run"]=="0":
			if cfg.checkInternet():
				os.system('pip install --upgrade pip')
				os.system('pip install keyboard')
				os.system('pip install numpy')
				os.system('pip install pygame')
				os.system('pip install PyTweening')
			else:
				os.system('pip install "'+os.getcwd()+'\\_commonredist\\keyboard.zip"')
				os.system('pip install "'+os.getcwd()+'\\_commonredist\\numpy.zip"')
				os.system('pip install "'+os.getcwd()+'\\_commonredist\\pygame.zip"')
				os.system('pip install "'+os.getcwd()+'\\_commonredist\\PyTweening.zip"')
			cfg.set("first_run","1")
			cfg.update()

	# SETS THE VALUE OF A CONFIG PARAMETER
	def set(cfg,name,value):
		cfg.items[name] = value

	# WRITES PARAMETERS TO THE CONFIG FILE
	def update(cfg):
		f = open("config","w")
		for key,value in cfg.items.items():
			f.write(key+"="+value+"\n")
		f.close()

	# GETS THE VALUES FROM THE CONFIG FILE
	def get(cfg):
		f = open("config","r")
		for index,line in enumerate(f):
			config_items = line.split("=")
			cfg.items[config_items[0].strip()] = config_items[1].strip()
		f.close()

	# CHECKS IF INTERNET IS AVAILABLE
	def checkInternet(cfg,host="8.8.8.8", port=53, timeout=3):
		try:
			socket.setdefaulttimeout(timeout)
			socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
			return True
		except socket.error as ex:
			print(ex)
			return False