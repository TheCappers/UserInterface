from Database import Database


class Sync:

    def __init__(self):
        self.__sync_status = False  # if it has started or not
        self.__sync_video = True
        self.__sync_screenshot = True
        self.__sync_mouse_action = True
        self.__sync_keystroke = True
        self.__sync_process = True
        self.__sync_network = True
        self.__sync_window_history = True
        self.__sync_system_call = True

    def getSyncStatus(self):
        return self.__sync_status

    def setVideoSync(self, value):  # the following would be used when interrupting
        self.__sync_video = value
        # add interuption if here

    def setScreenshotSync(self, value):
        self.__sync_screenshot = value

    def setMouseSync(self, value):
        self.__sync_mouse_action = value

    def setKeystrokSync(self, value):
        self.__sync_keystroke = value

    def setProcessSync(self, value):
        self.__sync_process = value

    def setNetworkSync(self, value):
        self.__sync_network = value

    def setWindowSync(self, value):
        self.__sync_window_history = value

    def setSystemCall(self, value):
        self.__sync_system_call = value
