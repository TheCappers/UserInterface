from recorders.recorded_data import RecordedData
import numpy

import os
import sys
import time
from PIL import ImageGrab
from PIL import Image
from matplotlib import pyplot as plt

from pynput import mouse
from pynput import keyboard

class ScreenshotRecorder(RecordedData):
		def __init__(self):
			RecordedData.__init__(self)
			self.isAutoRecord = True
			self._screenshot_data = self.get_recorded_data()
			self._screenshot_data['name'] = "Screenshot"
			self._screenshot_data['data'] = []
			self.image = None

			"""
			self.listener = keyboard.Listener(
				on_press=self.on_press
			)
			self.startScreenshotRecording()
			#self.lock = Lock()
			self.isRecording = True
			self.listener.start()

			self.__listener = mouse.Listener(
	            on_move=self._on_move,
	            on_click=self._on_click,
	            on_scroll=self._on_scroll)
	        self.__listener.start()

			def _on_move(self, x, y):
		        if self.__autorecording:
		            self.__mouse_action['data']['position'] = (x, y)
		            self.insert_to_db()
			"""



			# Setup the listener threads
			self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
			self.mouse_listener = mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll)

			# Start the threads and join them so the script doesn't end early
			self.keyboard_listener.start()
			self.mouse_listener.start()


		def on_press(self, key):
			if self.isAutoRecord:
				img = self.takeScreenshot()
				print(img)

		def on_release(self, key):
			if self.isAutoRecord:
				print("Key released: {0}".format(key))

		def on_click(self, x, y, button, pressed):
			if self.isAutoRecord:
				if pressed:
					print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
					#test view self.viewScreenshot()
				else:
					print('Mouse released at ({0}, {1}) with {2}'.format(x, y, button))

		def on_scroll(self, x, y, dx, dy):
			if self.isAutoRecord:
				print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


		def start(self):
			# ...or, in a non-blocking fashion:
			if self.isAutoRecord:
					return
			self.isAutoRecord = True
			#self.listener.join()
			print('start screenshot recordig')

		def stop(self):
			if not self.isAutoRecord:
					return
			self.isAutoRecord = False
			print('stop screenshot recording')

		def takeScreenshot(self):
			self.image = numpy.array(ImageGrab.grab())

		def viewScreenshot(self):
			viewable = Image.fromarray(self.image)
			#plt.imshow(viewable, interpolation='nearest')
			viewable.show()
			#viewable.save('screenshot.png')
			#viewable.show()
