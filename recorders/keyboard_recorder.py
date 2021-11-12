from pynput import keyboard
from recorders.recorded_data import RecordedData


class KeyboardRecorder(RecordedData):
	def __init__(self, isAutoRecord):
		RecordedData.__init__(self)
		self.isAutoRecord = False
		self._keystroke_data = self.get_recorded_data()
		self._keystroke_data['name'] = "Keystroke"
		self._keystroke_data['data'] = ''
		self.listener = keyboard.Listener()
		self.startKeyboardRecording()

	def startKeyboardRecording(self):
		# ...or, in a non-blocking fashion:
		if self.isAutoRecord:
			return
		self.isAutoRecord = True
		self.listener = keyboard.Listener(
			on_press=self.on_press
		)
		self.listener.start()

	def stopKeyboardRecording(self):
		if not self.isAutoRecord:
			return
		self.isAutoRecord = False

	def checkrecording(self):
		return self.isAutoRecord

	def on_press(self, key):
		if not self.checkrecording():
			return False
		self._keystroke_data['data'] = str(key).replace('\'', '')
		self.insert_to_db(self._keystroke_data)
		# print(format(key))
		print(str(key))

	# noinspection PyMethodMayBeStatic
	def on_release(self, key):
		# print('{0} released'.format(key))
		if key == keyboard.Key.esc:
			# Stop listener
			return False
