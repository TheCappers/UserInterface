from Database import Database
import threading
from Sync.sender import Sender


class Sync:

    def __init__(self):
        self.__listener = threading.Thread()
        self.video_list = []
        self.screenshot_list = []
        self.mouse_action_list = []
        self.keystroke_list = []
        self.process_list = []
        self.network_list = []
        self.window_history_list = []
        self.system_call_list = []
        self.sync_sender = Sender()

    def videoSync(self, ip_address):
        self.__listener = threading.Thread(target=self.sync_sender.start(self.video_list, ip_address))
        self.__listener.start()

    def screenshotSync(self, ip_address):
        self.__listener = threading.Thread(target=self.sync_sender.start(self.screenshot_list, ip_address))
        self.__listener.start()

    def mouseSync(self, ip_address):
        self.__listener = threading.Thread(target=self.sync_sender.start(self.mouse_action_list, ip_address))
        self.__listener.start()

    def keystrokSync(self, ip_address):
        self.__listener = threading.Thread(target=self.sync_sender.start(self.keystroke_list, ip_address))
        self.__listener.start()

    def processSync(self, ip_address):
        self.__listener = threading.Thread(target=self.sync_sender.start(self.process_list, ip_address))
        self.__listener.start()

    def networkSync(self, ip_address):
        self.__listener = threading.Thread(target=self.sync_sender.start(self.network_list, ip_address))
        self.__listener.start()

    def windowSync(self, ip_address):
        self.__listener = threading.Thread(target=self.sync_sender.start(self.window_history_list, ip_address))
        self.__listener.start()

    def systemCall(self, ip_address):
        self.__listener = threading.Thread(target=self.sync_sender.start(self.system_call_list, ip_address))
        self.__listener.start()

    def artifcateSpliter(self, item_list, ip_address):
        for item in item_list:
            if item.get('name') == "Keystroke":
                self.keystroke_list.append(item)
            if item.get('name') == "Mouse_Action":
                self.mouse_action_list.append(item)
            if item.get('name') == "Screenshot":
                self.screenshot_list.append(item)
            if item.get('name') == "Process":
                self.process_list.append(item)
            if item.get('name') == "Window_History":
                self.window_history_list.append(item)
            if item.get('name') == "System_Call":
                self.system_call_list.append(item)
            if item.get('name') == "Video":
                self.video_list.append(item)
            if item.get('name') == "Network":
                self.network_list.append(item)

        if self.video_list:
            self.videoSync(ip_address)
        if self.screenshot_list:
            self.screenshotSync(ip_address)
        if self.mouse_action_list:
            self.mouseSync(ip_address)
        if self.keystroke_list:
            self.keystrokSync(ip_address)
        if self.process_list:
            self.processSync(ip_address)
        if self.network_list:
            self.networkSync(ip_address)
        if self.window_history_list:
            self.windowSync(ip_address)
        if self.system_call_list:
            self.systemCall(ip_address)

    def start(self, item_list, ip_address):
        self.artifcateSpliter(item_list, ip_address)


# item_list = [
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Window_History', 'Keystroke': 'LOL', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']},
#
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Mouse_Action', 'Keystroke': 'Zsas', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']},
#
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Keystroke', 'Keystroke': 'Hsfdasdf', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']},
#
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Window_History', 'Keystroke': 'adfasdH', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']},
#
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Mouse_Action', 'Keystroke': 'fdgbsdfgbZ', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']},
#
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Keystroke', 'Keystroke': 'Hsdfgsdfg', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']},
#
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Window_History', 'Keystroke': 'sdfgsdvH', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']},
#
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Mouse_Action', 'Keystroke': 'Zzxcvxzcv', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']},
#
#     {'_id': '615b8dee3f96615d6166ead6', 'name': 'Keystroke', 'Keystroke': 'Hzxvczxrdfasdf', 'Date': '9/11/2022',
#      'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': ['David', 'Manny']}
#
#           ]
#
# receiver_ip = '192.168.239.131'
# sync = Sync()
# sync.start(item_list, receiver_ip)
