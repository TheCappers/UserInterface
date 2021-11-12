from recorders.recorded_data import RecordedData
from Database.Database import DataBase
import threading
import os


class WindowRecorder(RecordedData):

    def __init__(self):
        RecordedData.__init__(self)
        self.isAutoRecord = True
        self.windows = []
        self.__window_data = self.get_recorded_data()
        self.__window_data['name'] = "Window_History"
        self.__window_data['data'] = ''
        self.__listener = threading.Thread()
        self.start()

    def _window_cap(self):
        # GET WINDOWS OPEN AND PUT THEM ON A LIST
        capture = os.popen("wmctrl -l").read()
        capture = capture.split("\n")  # functionality
        del capture[-1]
        # print(capture)
        # EXTRACT THE WINDOW NAME FROM THE RESULT
        for window in capture:
            i = 0
            count = 0
            start_index = 0

            while count < 3:
                if window[i] == ' ':
                    count += 1
                    if count == 3:
                        start_index = i + 1
                i += 1

            # CREATE A LIST WITH JUST THE WINDOWS NAMES
            self.windows.append(window[start_index: len(window)])
            # print(self.windows)
        # INSERT ONE BY ONE INTO DATABASE
        for window in self.windows:
            self.__window_data['data'] = window
            # print(self.__window_data)
            self.insert_to_db(self.__window_data)

    def start(self):
        # print("RUNNING")
        self.__listener = threading.Thread(target=self._window_cap)
        if not self.isAutoRecord:
            self.isAutoRecord = True
        self.__listener.start()

    def stop(self):
        self.isAutoRecord = False
        self.__listener.join()
