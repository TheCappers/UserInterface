from recorders.recorded_data import RecordedData

class ScreenshotRecorder(RecordedData):
		def __init__(self, isAutoRecord):
			RecordedData.__init__(self)
			self.isAutoRecord = True
			self._screenshot_data = self.get_recorded_data()
			self._screenshot_data['name'] = "Screenshot"
			self._screenshot_data['data'] = ''

			"""
			self.listener = keyboard.Listener(
				on_press=self.on_press
			)
			self.startScreenshotRecording()
			#self.lock = Lock()
			self.isRecording = True
			self.listener.start()
			"""

		def startScreenshotRecording(self):
			# ...or, in a non-blocking fashion:
			if self.isAutoRecord:
					return
			self.isAutoRecord = True
			#self.listener.join()
			print('start screenshot recordig')

		def stopScreenshotRecording(self):
			if not self.isAutoRecord:
					return
			self.isAutoRecord = False
			print('stop screenshot recording')

		def checkrecording(self):
			return self.isAutoRecord


  		def detectMouseClick(self):
			return
			"""
				if self.checkrecording():
					self._keystroke_data['data'] = format(key)
					self.insert_to_db(self._keystroke_data)
					# print(format(key))
			"""
		def detectKeystroke(self):
			return
				"""print('{0} released'.format(
						key))
				if key == keyboard.Key.esc:
						# Stop listener
						return False
						"""

# kr.isAutoRecord = False
# kr.stopKeyboardRecording()
