# from recorders.recorded_data import RecordedData
# from Database.Database import DataBase
import os


class ScriptMaker:
    def __init__(self):
        # sample
        self.items_list = []

    def __keystroke(self, item):
        if len(item.get('data')) > 1:
            keystroke_string = "pyautogui.typewrite(['" + str(item.get('data')) + "'], interval=0.1)\nsleep(0.1)\n"
        else:
            keystroke_string = "pyautogui.typewrite('" + str(item.get('data')) + "', interval=0.1)\nsleep(0.1)\n"

        return keystroke_string

    # data: { position: [ 1967, 144 ], clicked: false, scroll: 0, button: '' },
    def __mouse_action(self, item):
        #print("MOUSE ACTIONS")

        coordinates = item.get("data").get("position")
        print(coordinates)
        mouse_movement_string = "pyautogui.moveTo("+str(coordinates[0])+","+str(coordinates[1])+", 2)\nsleep(0.1)\n"

        return mouse_movement_string

    def script(self, items_list):
        file_name = "demo_script_1.py"
        desk_top = os.path.join(os.environ["HOME"], "Desktop")
        dd_dir = desk_top + "/Downloads"
        if not os.path.exists(dd_dir):
            os.makedirs(dd_dir)
        with open(os.path.join(dd_dir, file_name), 'w') as file:
            # initialize script file
            file.write("import pyautogui\n")
            file.write("from time import sleep\n")
            file.write("\n")

            for item in items_list:
                # print(item.get("name"))
                if item.get('name') == "Keystroke":
                    file.write(self.__keystroke(item))

                if item.get('name') == "Mouse_Action":
                    file.write(self.__mouse_action(item))
        file.close()

#
# items_list = [{ '_id': '617f39e3acf707ca9b53b4f9', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F',
#                 'timestamp': '18:50:42 10/31/2021', 'name': 'Mouse_Action', 'data': { 'position': [ 1967, 144 ],
#                 'clicked': 'false', 'scroll': 0, 'button': '' }, 'tag': [], 'annotation': []}
#               ]

#             {'_id': '617f3a09acf707ca9b53e24b', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'H', 'tag': [], 'annotation': []},
#             {'_id': '617f3a09acf707ca9b53e278', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'E', 'tag': [], 'annotation': []},
#             {'_id': '617f3a0aacf707ca9b53e288', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'L', 'tag': [], 'annotation': []},
#             {'_id': '617f3a09acf707ca9b53e24b', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'L', 'tag': [], 'annotation': []},
#             {'_id': '617f3a09acf707ca9b53e278', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'O', 'tag': [], 'annotation': []},
#             {'_id': '617f3a0aacf707ca9b53e288', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': ' ', 'tag': [], 'annotation': []},
#             {'_id': '617f3a09acf707ca9b53e24b', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'E', 'tag': [], 'annotation': []},
#             {'_id': '617f3a09acf707ca9b53e278', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'N', 'tag': [], 'annotation': []},
#             {'_id': '617f3a0aacf707ca9b53e288', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'M', 'tag': [], 'annotation': []},
#             {'_id': '617f3a0aacf707ca9b53e288', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'enter', 'tag': [], 'annotation': []},
#             {'_id': '617f3a0aacf707ca9b53e288', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'enter', 'tag': [], 'annotation': []}
#         ]
#
#
# scmk = ScriptMaker()
#
# scmk.script(items_list)
