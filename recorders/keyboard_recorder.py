from pynput import keyboard
from pynput.keyboard import Key, Controller
from recorded_data import RecordedData
import time

class KeyboardRecorder(RecordedData):
		def __init__(self, isRecord):
			self.isRecord = isRecord
			self.listener = keyboard.Listener(
				on_press=self.on_press,
				on_release=self.on_release
			)
			self.keystroke = 'h'

		def startKeyboardRecording(self):
			# ...or, in a non-blocking fashion:
			self.listener.start()
			print('start keyboard recordig')

		def stopKeyboardRecording(self):
			self.listener.stop()
			print('stop keyboard recording')

		def on_press(self, key):
				try:
						self.keystroke = key.char
						print('alphanumeric key {0} pressed'.format(
								key.char))
				except AttributeError:
						print('special key {0} pressed'.format(
								key))
						self.keystroke = key

		def on_release(self, key):
				print('{0} released'.format(
						key))
				if key == keyboard.Key.esc:
						# Stop listener
						return False


r = RecordedData()
k = KeyboardRecorder(True)
"""
k.startKeyboardRecording()
time.sleep(4)
k.stopKeyboardRecording()"""
r.recorded_data['name'] = "keystroke"
"""m.start()
time.sleep(2)
m.stop()"""
r.recorded_data['data'] = k.keystroke
print(r.recorded_data['name'])
print(r.recorded_data['data'])
