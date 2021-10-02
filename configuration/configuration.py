'''
Will apply logical configuration settings as
given by the user
'''
import shutil


class Configuration:
    def __init__(self):  # configurator constructor
        self.__threshold = 90  # interpret as percent
        # can be affected by all gui recording buttons checkmarks etc\
        self.__universal_on = True  # automatically on
        self.__keystroke_on = True
        self.__mouse_action_on = True
        # here we can include more attributes for other items.

    # getters and setters
    def getThreshold(self):
        return self.__threshold

    def getUniversalOn(self):
        return self.__universal_on

    def getKeystrokeOn(self):
        return self.__keystroke_on

    def getMouseActionOn(self):
        return self.__mouse_action_on

    def setThreshold(self, threshold_value):
        self.__threshold = threshold_value

    def setUniversalOn(self, universal_value):  # applies default values
        self.__universal_on = universal_value
        if universal_value:
            self.setKeystroke(True)
            self.setMouseAction(True)
        else:
            self.setKeystroke(False)
            self.setMouseAction(False)

    def setKeystroke(self, keystroke_value):
        self.__keystroke_on = keystroke_value

    def setMouseAction(self, mouse_value):
        self.__mouse_action_on = mouse_value

    def storage_alert(self):
        total, used, free = shutil.disk_usage("/")

        total = total // (2 ** 30)  # gb representation
        used = used // (2 ** 30)
        # hist = [self.getMouseActionOn(), self.getKeystrokeOn()]

        if ((used / total) * 100) >= self.__threshold:  # if we meet the threshold
            self.setUniversalOn(False)  # turn off all recordings
        # probably do not need this
        '''
        else:
            self.setMouseAction(hist[0])
            self.setKeystroke(hist[1])
        '''