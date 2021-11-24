from Database.Database import DataBase
import threading
from bson.objectid import ObjectId
from pymongo import MongoClient
from view.sync_tab.sync import Sync


class Sender:
    def __init__(self):
        self.__listener = threading.Thread()
        self.__db = DataBase()
        self.__db2 = ''
        self.keystroke_collection = ''
        self.mouse_collection = ''
        self.screenshot_collection = ''
        self.process_collection = ''
        self.windows_collection = ''
        self.syscall_collection = ''
        self.video_collection = ''
        self.network_collection = ''
        self.sync_percentage = 0
        self.artifact_type = ''
        self.sync_complete = False

    def connect_2db(self, item_list, receiver_ip, tab3_widget):
        db_server_url = 'mongodb://' + str(receiver_ip) + ':27017/'
        # print('Connecting to:', db_server_url)
        client = MongoClient(db_server_url)
        self.__db2 = client['AVERT']
        self.keystroke_collection = self.__db2["keystroke_collection"]
        self.mouse_collection = self.__db2["mouse_collection"]
        self.screenshot_collection = self.__db2["screenshot_collection"]
        self.process_collection = self.__db2["process_collection"]
        self.windows_collection = self.__db2["windows_collection"]
        self.syscall_collection = self.__db2["syscall_collection"]
        self.video_collection = self.__db2["video_collection"]
        self.network_collection = self.__db2["network_collection"]

        self.collection_type(item_list, tab3_widget)

    def collection_type(self, item_list, tab3_widget):
        if item_list[0].get('name') == "Keystroke":
            self.sync_2db(self.keystroke_collection, item_list, tab3_widget)
        if item_list[0].get('name') == "Mouse_Action":
            self.sync_2db(self.mouse_collection, item_list, tab3_widget)
        if item_list[0].get('name') == "Screenshot":
            self.sync_2db(self.screenshot_collection, item_list, tab3_widget)
        if item_list[0].get('name') == "Process":
            self.sync_2db(self.process_collection, item_list, tab3_widget)
        if item_list[0].get('name') == "Window_History":
            self.sync_2db(self.windows_collection, item_list, tab3_widget)
        if item_list[0].get('name') == "System_Call":
            self.sync_2db(self.syscall_collection, item_list, tab3_widget)
        if item_list[0].get('name') == "Video":
            self.sync_2db(self.video_collection, item_list, tab3_widget)
        if item_list[0].get('name') == "Network":
            self.sync_2db(self.network_collection, item_list, tab3_widget)
        self.sync_complete = True

    def sync_2db(self, collection, item_list, tab3_widget):
        synced_count = 0
        items_matched = False
        # tab3_widget.mouseaction_frame.progress_bar.setValue(3)

        for item in item_list:
            for entry in collection.find({}):
                for key, value in entry.items():
                    if key == '_id':
                        pass
                    elif item.get(key) == value:
                        items_matched = True
                    else:
                        items_matched = False
                        break

                if items_matched:
                    break

            if items_matched:
                synced_count += 1
                self.calculate_percentage(len(item_list), synced_count, item.get('name'), tab3_widget)
                pass
            else:
                # not a duplicate so we added it to the DATABASE
                item.update({"_id": ObjectId().__str__()})
                collection.insert_one(item)
                synced_count += 1
                self.calculate_percentage(len(item_list), synced_count, item.get('name'), tab3_widget)
        return None

    def calculate_percentage(self, total_items, items_synced, artifact_type, tab3_widget):
        sync_percentage = int((items_synced / total_items)*100)
        if artifact_type == "Keystroke":
            tab3_widget.keystroke_frame.progress_bar.setValue(sync_percentage)
        if artifact_type == "Mouse_Action":
            tab3_widget.mouseaction_frame.progress_bar.setValue(sync_percentage)
        if artifact_type == "Screenshot":
            tab3_widget.stillscreenshot_frame.progress_bar.setValue(sync_percentage)
        if artifact_type == "Process":
            tab3_widget.process_frame.progress_bar.setValue(sync_percentage)
        if artifact_type == "Window_History":
            tab3_widget.windowhistory_frame.progress_bar.setValue(sync_percentage)
        if artifact_type == "System_Call":
            tab3_widget.systemcall_frame.progress_bar.setValue(sync_percentage)
        if artifact_type == "Video":
            tab3_widget.video_frame.progress_bar.setValue(sync_percentage)
        if artifact_type == "Network":
            tab3_widget.networkactivitydata_frame.progress_bar.setValue(sync_percentage)
        # print(sync_percentage, artifact_type)

    def getPercentageInfo(self):
        return self.sync_percentage, artifact_type

    def start(self, item_list, receiver_ip, tab3_widget):
        self.connect_2db(item_list, receiver_ip, tab3_widget)

    def isSyncComplete(self):
        return self.status
