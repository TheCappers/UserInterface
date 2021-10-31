'''
Will apply logical configuration settings as
given by the user
'''
import shutil
from recorders import keyboard_recorder, mouse_recorder, systemcall_recorder, process_recorder, window_recorder,
    screenshot_recorder, video_recorder

# global recorders
keyboard = keyboard_recorder.KeyboardRecorder(True)
mouse = mouse_recorder.MouseRecorder()
system_call = systemcall_recorder.SytemsCallRecorder()
system_call.systemcallrecorder_start()
window_history = window_recorder.WindowRecorder()
process = process_recorder.ProcessRecorder()
screenshot = screenshot_recorder.ScreenshotRecorder()
video = video_recorder.VideoRecorder()
process.start()


# screenshot =


class Configuration:
    def __init__(self):  # configurator constructor
        self.__threshold = 70  # interpret as percent
        # can be affected by all gui recording buttons checkmarks etc\
        self.__universal_on = True  # automatically on
        self.__keystroke_on = True
        self.__mouse_action_on = True
        self.__process_on = True
        self.__system_call_on = True
        self.__window_history_on = True
        self.__screenshot_on = True
        self.__video_on = True
        '''
        Here we add the new records values
        '''

        # here we can include more attributes for other items.
        # include artifact recorders start actions

    # getters and setters
    # all parameters treated as booleans

    def getThreshold(self):
        return self.__threshold

    def getUniversalOn(self):
        return self.__universal_on

    def getKeystrokeOn(self):
        return self.__keystroke_on

    def getMouseActionOn(self):
        return self.__mouse_action_on

    def getSystemCallOn(self):
        return self.__system_call_on

    def getScreenshotOn(self):
        return self.__screenshot_on

    def getVideoOn(self):
        return self.__video_on

    def getWindowHistory(self):
        return self.__window_history_on

    def getProcessOn(self):
        return self.__process_on

    def setThreshold(self, threshold_value):
        self.__threshold = threshold_value

    def setUniversalOn(self, universal_value):  # applies default values
        self.__universal_on = universal_value
        # ('From Config: ', self.__universal_on)
        if universal_value:
            self.setKeystroke(True)
            self.setMouseAction(True)
            self.setScreenshot(True)
            self.setVideo(True)
            self.setSystemCall(True)
            self.setProcess(True)
            self.setWindowHistory(True)
            # recorders
        else:
            self.setKeystroke(False)
            self.setProcess(False)
            self.setSystemCall(False)
            self.setMouseAction(False)
            self.setScreenshot(False)
            self.setVideo(False)
            self.setWindowHistory(False)
            # recorders

    def setKeystroke(self, keystroke_value):
        self.__keystroke_on = keystroke_value
        keyboard.isRecord = keystroke_value  # updating recording value
        # controlling the recorder
        if keystroke_value:
            keyboard.startKeyboardRecording()
        else:
            keyboard.stopKeyboardRecording()

    def setMouseAction(self, mouse_value):
        self.__mouse_action_on = mouse_value
        # controlling the mouse action recording tool
        if mouse_value:
            mouse.start()
        else:
            mouse.stop()

    def setSystemCall(self, sys_call_value):
        self.__system_call_on = sys_call_value
        # controlling the recording tool
        # system_call.willRecord = sys_call_value
        if sys_call_value:
            system_call.systemcallrecorder_start()
        else:
            system_call.systemcallrecorder_end()

    def setScreenshot(self, screenshot_value):
        self.__screenshot_on = screenshot_value
        # controlling the recording tool
        # system_call.willRecord = sys_call_value
        if screenshot_value:
            screenshot.start()
        else:
            screenshot.stop()

    def setVideo(self, video_value):
        self.__video_on = video_value
        # controlling the recording tool
        # system_call.willRecord = sys_call_value
        if video_value:
            video.start()
        else:
            video.stop()


    def setWindowHistory(self, window_history_value):
        self.__window_history_on = window_history_value
        # controlling the recording tool
        if window_history_value:
            window_history.start()
        else:
            window_history.stop()

    def setProcess(self, process_value):
        self.__process_on = process_value
        # controlling the recording tool
        if process_value:
            process.start()
        else:
            process.stop()

    def manualScreenshot(self, manuel_value):
        return

    def storage_alert(self):  # return value to send error
        total, used, free = shutil.disk_usage("/")

        total = total // (2 ** 30)  # gb representation
        used = used // (2 ** 30)
        # hist = [self.getMouseActionOn(), self.getKeystrokeOn()]

        if ((used / total) * 100) >= self.__threshold:  # if we meet the threshold
            return True
        else:
            return False  # all good nothing going on
        # probably do not need this
