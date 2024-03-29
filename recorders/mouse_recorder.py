from pynput import mouse
from recorders.recorded_data import RecordedData

from Database.Database import DataBase

'''
Sets up listener. To start the listener invoke start() and to stop it invoke stop()
'''


class MouseRecorder(RecordedData):

    def __init__(self):
        RecordedData.__init__(self)
        self.__autorecording = True
        self.__mouse_action = self.get_recorded_data()
        self.__mouse_action['name'] = 'Mouse_Action'
        self.__mouse_action['data'] = {"position": (
            0, 0), "clicked": False, "scroll": 0, "button": ''}
        self.__mock_db = []
        self.__mock = False

        self.__db = DataBase()

        self.__listener = mouse.Listener(
            on_move=self._on_move,
            on_click=self._on_click,
            on_scroll=self._on_scroll)
        self.__listener.start()

    def _on_move(self, x, y):
        if self.__autorecording:
            self.__mouse_action = self.get_recorded_data() 
            self.__mouse_action['data']['position'] = (x, y)
            self.insert_to_db()

    def _on_click(self, x, y, button, pressed):
        if self.__autorecording:
            if pressed:
                self.__mouse_action = self.get_recorded_data() 
                self.__mouse_action['data']['clicked'] = True
                if str(button) == "Button.left":
                    self.__mouse_action['data']['button'] = "left"
                elif str(button) == "Button.right":
                    self.__mouse_action['data']['button'] = "right"
                else:
                    self.__mouse_action['data']['button'] = "middle"
            else:
                self.__mouse_action = self.get_recorded_data() 
                self.__mouse_action['data']['clicked'] = False
                self.__mouse_action['data']['button'] = ''
            
            self.insert_to_db()

    def _on_scroll(self, x, y, dx, dy):
        if self.__autorecording:
            self.__mouse_action = self.get_recorded_data() 
            self.__mouse_action['data']['scroll'] = dy
            self.insert_to_db()

    def start(self):
        if self.__autorecording:
            return
        self.__autorecording = True

    def stop(self):
        if not self.__autorecording:
            return
        self.__autorecording = False

    def terminate(self):
        self.__listener.stop()

    def insert_to_db(self):
        if not self.__mock:
            self.__db.query_db("post", self.__mouse_action, "")
        else:
            self.__mock_db.append(self.__mouse_action)

    def print_mock_db(self):
        if self.__mock:
            print("first value stored: {0}\nstored items: {1}".format(
                self.__mock_db[-1], len(self.__mock_db)))

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
