from recorders.keyboard_recorder import KeyboardRecorder


class Controller_:
	def __init__(self):
		self.isRecordKeyboard = True
		KeyboardRecorder(self.isRecordKeyboard)


