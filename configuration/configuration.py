'''
Will apply logical configuration settings as
given by the user
'''
import shutil
from recorders import keyboard_recorder, mouse_recorder, systemcall_recorder, process_recorder, window_recorder,screenshot_recorder

# global recorders
keyboard = keyboard_recorder.KeyboardRecorder(True)
mouse = mouse_recorder.MouseRecorder()
system_call = systemcall_recorder.SytemsCallRecorder()
#system_call.systemcallrecorder_start()
window_history = window_recorder.WindowRecorder()
#window_history.start()
process = process_recorder.ProcessRecorder()
screenshot = screenshot_recorder.ScreenshotRecorder()
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
        # self.__screenshot_on = True
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
        return

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
            # recorders
            keyboard.isRecord = universal_value  # updating recording value
            keyboard.startKeyboardRecording()
            mouse.start()
            screenshot.start()
        else:
            self.setKeystroke(False)
            self.setMouseAction(False)
            self.setScreenshot(False)
            # recorders
            keyboard.isRecord = universal_value  # updating recording value
            keyboard.stopKeyboardRecording()
            mouse.stop()
            screenshot.stop()


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
        if sys_call_value:
            system_call.systemcallrecorder_start()
        else:
            system_call.systemcallrecorder_end()

    def setScreenshot(self, screenshot_value):
        return

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
