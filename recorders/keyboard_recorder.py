from pynput import keyboard
from pynput.keyboard import Key, Controller
from recorders.recorded_data import RecordedData
from threading import Lock

class KeyboardRecorder(RecordedData):
		def __init__(self, isAutoRecord):
			RecordedData.__init__(self)
			self.isAutoRecord = True
			self._keystroke_data = self.get_recorded_data()
			self._keystroke_data['name'] = "Keystroke"
			self._keystroke_data['data'] = ''
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
			#print('start keyboard recordig')

		def stopKeyboardRecording(self):
			if not self.isAutoRecord:
					return
			self.isAutoRecord = False
			#print('stop keyboard recording')

		def checkrecording(self):
			return self.isAutoRecord

		def on_press(self, key):
				if self.checkrecording():
					self._keystroke_data['data'] = str(key).replace('\'', '')
					self.insert_to_db(self._keystroke_data)
					# print(format(key))

		def on_release(self, key):
				print('{0} released'.format(
						key))
				if key == keyboard.Key.esc:
						# Stop listener
						return False

# kr.isAutoRecord = False
# kr.stopKeyboardRecording()