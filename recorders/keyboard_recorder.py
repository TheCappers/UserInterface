from pynput import keyboard
from pynput.keyboard import Key, Controller
from recorders.recorded_data import RecordedData


class KeyboardRecorder(RecordedData):
		def __init__(self, isRecord):
			self.isRecord = isRecord
			self.listener = keyboard.Listener(
				on_press=self.on_press,
				on_release=self.on_release
			)

		def startKeyboardRecording(self):
			# ...or, in a non-blocking fashion:
			self.listener.start()
			print('start keyboard recordig')

		def stopKeyboardRecording(self):
			self.listener.stop()
			print('stop keyboard recording')

		def on_press(self, key):
				try:
						print('alphanumeric key {0} pressed'.format(
								key.char))
						self.get_timestamp()
				except AttributeError:
						print('special key {0} pressed'.format(
								key))

		def on_release(self, key):
				print('{0} released'.format(
						key))
				if key == keyboard.Key.esc:
						# Stop listener
						return False