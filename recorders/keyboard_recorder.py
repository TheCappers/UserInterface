from pynput import keyboard
from pynput.keyboard import Key, Controller
from recorders.recorded_data import RecordedData
from threading import Lock

class KeyboardRecorder(RecordedData):
		def __init__(self, isAutoRecord):
			self.isAutoRecord = True
			self.listener = keyboard.Listener(
				on_press=self.on_press
			)
			self.startKeyboardRecording()
			#self.lock = Lock()
			self.isRecording = True
			self.listener.start()

		def startKeyboardRecording(self):
			# ...or, in a non-blocking fashion:
			if self.isAutoRecord:
					return
			self.isAutoRecord = True
			#self.listener.join()
			print('start keyboard recordig')

		def stopKeyboardRecording(self):
			if not self.isAutoRecord:
					return
			self.isAutoRecord = False
			print('stop keyboard recording')

		def checkrecording(self):
			return self.isAutoRecord

		def on_press(self, key):
				if self.checkrecording():
					try:
							print('alphanumeric key {0} pressed'.format(
									key.char))
							self.post = {
								"_id": "333",
								"name": "Keystroke",
								"Date": "9/11/2111",
								"IP Address": "1.1.1.1",
								"Keystroke": key.char
							}
							# self.save_recorded_data({"Keystroke": key.char, "name": "Keystroke"})
					except AttributeError:
							print('special key {0} pressed'.format(
									key))


		def on_release(self, key):
				print('{0} released'.format(
						key))
				if key == keyboard.Key.esc:
						# Stop listener
						return False

# kr.isAutoRecord = False
# kr.stopKeyboardRecording()