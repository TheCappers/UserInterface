from recorders.recorded_data import RecordedData
from Database.Database import DataBase
import imageio

import numpy as np
import os
import sys
import time
from PIL import ImageGrab
from PIL import Image

from pynput import mouse
from pynput import keyboard
import datetime


class VideoRecorder(RecordedData):
    def __init__(self):
        RecordedData.__init__(self)
        self.isAutoRecord = True
        self._video_data = self.get_recorded_data()
        self._video_data['name'] = "Video"
        self._video_data['data'] = {'path': "", 'size': "", 'resolution': "", 'frame_rate': ""}
        self._video_started = False
        self._frame_rate = 15
        self._duration = 5
        self._writer = ''
        self._start_time = 'default'
        self.__db = DataBase()

        # Setup the listener threads
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.mouse_listener = mouse.Listener(on_click=self.on_click,on_move=self.on_move)
        # Start the threads and join them so the script doesn't end early
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def on_press(self, key):
        if self._video_started:
            self._duration = 5

    def on_release(self, key):
        if self._video_started:
            self._duration = 5

    def on_click(self, x, y, button, pressed):
        if self._video_started:
            if pressed:
                self._duration = 5

    def on_move(self, x, y):
        if self._video_started:
            self._duration = 5

    def start(self):
        if self._video_started:
            return

        self._video_started = True
        self._start_time = str(datetime.datetime.now().strftime("%Y-%m-%d~%H:%M:%S"))
        isExist = os.path.exists("Videos")
        if not isExist:
            os.mkdir("Videos")
        self._video_data['data']['path'] = "Videos/" + self._start_time + '.mp4'
        self._writer=imageio.get_writer(self._video_data['data']['path'], fps=self._frame_rate)
        print("start video")

    def stop(self):
        if not self._video_started:
            return
        self._video_started = False
        self.writer.close()
        self.image.save(self._video_data['data']['path'])
        file_size = os.path.getsize(self._video_data['data']['path'])
        file_type = os.path.splitext(self._video_data['data']['path'])[-1]
        self._video_data['data']['size'] = file_size
        self._video_data['data']['type'] = file_type
        #TODO: self.insert_to_db()
        print('stop video recording')

    def takeVideo(self):
        self.image = ImageGrab.grab()
        for i in range(fps*duration):
            img = np.array(ImageGrab.grab())
            self.writer.append_data(img)


'''
    def viewVideo(self):
        os.system("xdg-open " + self._video_data['data']['path'])
        time.sleep(3)

    def insert_to_db(self):
        self.__db.query_db("post", self._video_data, "")
'''
