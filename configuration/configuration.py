'''
Will apply logical configuration settings as
given by the user
'''
import shutil
from recorders import keyboard_recorder, mouse_recorder

# global recorders
keyboard = keyboard_recorder.KeyboardRecorder(True)
mouse = mouse_recorder.MouseRecorder()


class Configuration:
    def __init__(self):  # configurator constructor
        self.__threshold = 70  # interpret as percent
        # can be affected by all gui recording buttons checkmarks etc\
        self.__universal_on = True  # automatically on
        self.__keystroke_on = True
        self.__mouse_action_on = True
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
        return

    def getScreenshotOn(self):
        return

    def getWindowHistory(self):
        return

    def getProcessOn(self):
        return

    def setThreshold(self, threshold_value):
        self.__threshold = threshold_value

    def setUniversalOn(self, universal_value):  # applies default values
        self.__universal_on = universal_value
        print('From Config: ', self.__universal_on)

        if universal_value:
            self.setKeystroke(True)
            self.setMouseAction(True)
            # recorders
            keyboard.isRecord = universal_value  # updating recording value
            keyboard.startKeyboardRecording()
            mouse.start()
        else:
            self.setKeystroke(False)
            self.setMouseAction(False)
            # recorders
            keyboard.isRecord = universal_value  # updating recording value
            keyboard.stopKeyboardRecording()
            mouse.stop()

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

    def setSystemCalls(self, sys_call_value):
        return

    def setScreenshot(self, screenshot_value):
        return

    def setWindowHistory(self, window_history_value):
        return

    def setProcess(self, process_value):
        return

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
