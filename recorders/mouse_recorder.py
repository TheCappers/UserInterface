from pynput import mouse
from recorders.recorded_data import RecordedData

from Database.Database import DataBase
'''
Sets up listener. To start the listener invoke start() and to stop it invoke stop()
'''
class MouseRecorder(RecordedData):

    def __init__(self):
        self.autorecording = True
        self.__listener = mouse.Listener(
            on_move=self.__on_move,
            on_click=self.__on_click,
            on_scroll=self.__on_scroll)
        self.__listener.start()
        self.mouse_movement = {"position": (0,0), "clicked": False}

    def __on_move(self, x, y):
        self.mouse_movement['position'] = (x,y)
        if self.autorecording:
            print(self.mouse_movement)

    def __on_click(self, x, y, button, pressed):
        if self.autorecording:
            if pressed:
                self.mouse_movement['clicked'] = True
            else:
                self.mouse_movement['clicked'] = False

    def __on_scroll(self, x, y, dx, dy):
        if self.autorecording:
            print('Scrolled {0} at {1}'.format(
                'down' if dy < 0 else 'up',
                (x, y)))

    def start(self):
        if self.autorecording:
           return 
        self.autorecording = True

    def stop(self):
        if not self.autorecording:
            return 
        self.autorecording = False

    def terminate(self):
        self.__listener.stop()


# This is for getting full recording data
# r = RecordedData()
# m = MouseRecorder()
# r.recorded_data['type'] = "mouse_movement"
# r.recorded_data['data'] = m.mouse_movement

# print(r.recorded_data)

# Schema for sending the data (keystroke)
# post_1 = {
#     "name": "Keystroke",
#     "Keystroke": "H",
#     "Date": "9/11/2021",
#     "IP Address": "1.2.3.4",
# }
# Schema for sending the data (mouse action)
# post_2 = {
#     "name": "Mouse_Action",
#     "coordinate": (200,402),
#     "click": True,
#     "date": "9/11/2021",
#     "ip_address": "1.2.3.4",
#     "mac_address": "39:0f:b2:29:48"
# }

# db = DataBase()
# db.query_db("post", post_1, "")
# print(db.query_db("find", post_1, ""))