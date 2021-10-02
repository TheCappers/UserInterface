from pynput import keyboard
from pynput.keyboard import Key, Controller
from recorders.recorded_data import RecordedData


class KeyboardRecorder(RecordedData):
		def __init__(self, isRecord):
			self.isRecord = isRecord
			if self.isRecord:
				print("true")
				self.startKeyboardRecording()
			else:
				print("nope")
				self.stopKeyboardRecording()

		def startKeyboardRecording(self):
			# ...or, in a non-blocking fashion:
			listener = keyboard.Listener(
    		on_press=self.on_press,
   			on_release=self.on_release)
			listener.start()
			print('start keyboard recordig')

		def stopKeyboardRecording(self):
			"""listener.stop(
				StopException = True
			)"""
			print('stop keyboard recording')

		def on_press(self, key):
				try:
						print('alphanumeric key {0} pressed'.format(
								key.char))
				except AttributeError:
						print('special key {0} pressed'.format(
								key))

		def on_release(self, key):
				print('{0} released'.format(
						key))
				if key == keyboard.Key.esc:
						# Stop listener
						return False