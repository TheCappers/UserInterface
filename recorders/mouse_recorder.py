from pynput import mouse
from recorders.recorded_data import RecordedData
'''
Sets up listener. To start the listener invoke start() and to stop it invoke stop()
'''
class MouseRecorder(RecordedData):

    def __init__(self):
        self.__listener = mouse.Listener(
            on_move=self.__on_move,
            on_click=self.__on_click,
            on_scroll=self.__on_scroll)

    def __on_move(self, x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    def __on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))

    def __on_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    # start method goes here to 
    def start(self):
        self.__listener.start()

    # stop method goes here (stops the listener)
    def stop(self):
        self.__listener.stop()

