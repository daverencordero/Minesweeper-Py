class StateHandler:
	states = {}
	current_state = None

	# ADDS A STATE TO THE STATE HANDLER CLASS
	@staticmethod
	def addState(name:str,state):
		StateHandler.states[name]=state

	# SETS THE STATE 
	@staticmethod
	def setState(name):
		if(name in StateHandler.states):
			StateHandler.current_state = StateHandler.states[name]
		else:
			print("StateHandler: '%s' state is not found" %name)
	
	# GETS A SPECIFIC STATE
	@staticmethod
	def getState(name):
		return StateHandler.states[name]

	# RETURNS THE CURRENT STATE
	@staticmethod
	def getCurrentState():
		return StateHandler.current_state