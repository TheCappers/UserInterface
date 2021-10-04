from pynput import mouse
from recorders.recorded_data import RecordedData

from Database.Database import DataBase
'''
Sets up listener. To start the listener invoke start() and to stop it invoke stop()
'''
class MouseRecorder(RecordedData):

    def __init__(self):
        RecordedData.__init__(self)
        self._autorecording = True
        
        self._mouse_action = self.get_recorded_data()
        self._mouse_action['name'] = 'Mouse_Action'
        self._mouse_action['data'] = {"position": (0,0), "clicked": False, "scroll": 0, "button": ''}

        self._mock_db = []

        self._mock = False

        self._db = DataBase()

        self._listener = mouse.Listener(
            on_move=self._on_move,
            on_click=self._on_click,
            on_scroll=self._on_scroll)
        self._listener.start()

    def _on_move(self, x, y):
        if self._autorecording:
            self._mouse_action['data']['position'] = (x,y)
            self.insert_to_db()

    def _on_click(self, x, y, button, pressed):
        if self._autorecording:
            if pressed:
                self._mouse_action['data']['clicked'] = True
                self._mouse_action['data']['button'] = button
            else:
                self._mouse_action['data']['clicked'] = False
                self._mouse_action['data']['button'] = ''
            self.insert_to_db()

    def _on_scroll(self, x, y, dx, dy):
        if self._autorecording:
            self._mouse_action['data']['scroll'] = dy
            self.insert_to_db()

    def start(self):
        if self._autorecording:
           return 
        self._autorecording = True

    def stop(self):
        if not self._autorecording:
            return 
        self._autorecording = False

    def terminate(self):
        self._listener.stop()

    def insert_to_db(self):
        if not self._mock:
            self._db.query_db("post", self._mouse_action, "")
        else:
            self._mock_db.append(self._mouse_action)

    def print_mock_db(self):
        if self.mock:
            print("first value stored: {0}\nstored items: {1}".format(self._mock_db[-1], len(self._mock_db)))


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