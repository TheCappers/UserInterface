from recorders.recorded_data import RecordedData
from Database.Database import DataBase
import numpy

import os
import sys
import time
from PIL import ImageGrab
from PIL import Image

from pynput import mouse
from pynput import keyboard
import datetime

class ScreenshotRecorder(RecordedData):
		def __init__(self):
			RecordedData.__init__(self)
			self.isAutoRecord = True
			self._screenshot_data = self.get_recorded_data()
			self._screenshot_data['name'] = "Screenshot"
			self._screenshot_data['data'] = {'path': "", 'size' : "", 'type' : ""}
			self.image = None
			self.__db = DataBase()

			# Setup the listener threads
			self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
			self.mouse_listener = mouse.Listener(on_click=self.on_click)

			# Start the threads and join them so the script doesn't end early
			self.keyboard_listener.start()
			self.mouse_listener.start()


		def on_press(self, key):
			if self.isAutoRecord:
				self.takeScreenshot()

		def on_release(self, key):
			if self.isAutoRecord:
				print("Key released: {0}".format(key))

		def on_click(self, x, y, button, pressed):
			if self.isAutoRecord:
				if pressed:
					self.takeScreenshot()
					print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))


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
			date_time = str(datetime.datetime.now().strftime("%Y-%m-%d~%H:%M:%S"))
			self.image = ImageGrab.grab()
			isExist = os.path.exists("Images")
			if not isExist:
				os.mkdir("Images")
			self._screenshot_data['data']['path'] = "Images/" + date_time + '.png'
			self.image.save(self._screenshot_data['data']['path'])
			file_size = os.path.getsize(self._screenshot_data['data']['path'])
			file_type = os.path.splitext(self._screenshot_data['data']['path'])[-1]

			self._screenshot_data['data']['size'] = file_size
			self._screenshot_data['data']['type'] = file_type
			self.insert_to_db()

		def viewScreenshot(self):
			os.system("xdg-open " + self._screenshot_data['data']['path'])
			time.sleep(3)

		def insert_to_db(self):
			self.__db.query_db("post", self._screenshot_data, "")
