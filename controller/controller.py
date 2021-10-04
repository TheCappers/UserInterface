from recorders.keyboard_recorder import KeyboardRecorder
from configuration import configuration


class Controller:
    def __init__(self):
        self.config = configuration.Configuration()

    def universalRecording(self, signal):  # automatically records
        self.config.setUniversalOn(signal)

    def mouseActionRecording(self, signal):
        self.config.setMouseAction(signal)

    def keyboardRecording(self, signal):
        self.config.setKeystroke(signal)

    def storageRecording(self, amount):
        self.config.setThreshold(amount)
        full = self.config.storage_alert()
        return full  # send to view

    def export(self, item):  # here is where we would use the database to export
        return

    def view(self, item):  # here is where we would connect to database to view an item in avert
        return item

    def searchDB(self, item):  # here is where we would connect to database to pull up results
        # logic for how it will be viewed
        return

    def annotationAdd(self, annot, item): # here we update the item in the DB with an annotation
        return