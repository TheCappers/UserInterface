import os
from Database.Database import DataBase

class ScriptMaker:
    def __init__(self):
        # sample
        self.items_list = []

    def __keystroke(self, item):
        if len(item.get('data')) > 1:
            keystroke_string = "pyautogui.press('" + str(item.get('data')).replace('Key.', '') + "', interval=0.1)\n"
            # print(keystroke_string)
        else:
            keystroke_string = "pyautogui.typewrite('" + str(item.get('data')) + "', interval=0.1)\n"
            # print(keystroke_string)
        return keystroke_string

    # data: { position: [ 1967, 144 ], clicked: false, scroll: 0, button: '' },
    def __mouse_action(self, item):
        coordinates = item.get("data").get("position")
        if item.get("data").get("clicked"):
            mouse_movement_string = "pyautogui.click("+str(coordinates[0])+", "+str(coordinates[1])+")\n"
        else:
            mouse_movement_string = "pyautogui.moveTo(" + str(coordinates[0]) + ", " + str(coordinates[1]) + ", 0.1)\n"
        return mouse_movement_string

    def script(self, items_list):
        items_list = self.sort_list(items_list)

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

    def sort_list(self, item_list):
        sorted_list = sorted(item_list, key=lambda d: d['milliseconds'])
        # for i in sorted_list:
        #     print(i)
        return sorted_list
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
# db = DataBase()
# items_list = db.query_db('get_type', '', 'Keystroke')

# items_list += db.query_db('get_type', '', 'Mouse_Action')

# scmk = ScriptMaker()
#
# scmk.script(items_list)
