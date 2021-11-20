import os
from Database.Database import DataBase
import threading, socket
import ast
from pymongo import MongoClient


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

    def connect_2db(self, item_list, receiver_ip):
        db_server_url = 'mongodb://'+str(receiver_ip)+':27017/'
        print('Connecting to:', db_server_url)
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

    def collection_type(self, item_list):
        if item_list[0].get('name') == "Keystroke":
            self.sync_2db(self.keystroke_collection, item_list)
        if item_list[0].get('name') == "Mouse_Action":
            self.sync_2db(self.mouse_collection, item_list)
        if item_list[0].get('name') == "Screenshot":
            self.sync_2db(self.screenshot_collection, item_list)
        if item_list[0].get('name') == "Process":
            self.sync_2db(self.process_collection, item_list)
        if item_list[0].get('name') == "Window_History":
            self.sync_2db(self.windows_collection, item_list)
        if item_list[0].get('name') == "System_Call":
            self.sync_2db(self.syscall_collection, item_list)
        if item_list[0].get('name') == "Video":
            self.sync_2db(self.video_collection, item_list)
        if item_list[0].get('name') == "Network":
            self.sync_2db(self.network_collection, item_list)


    def sync_2db(self, collection, item_list):
        break_flag = True

        while break_flag:

            for entry in collection.find({}):
                for item in item_list:

                    for key, value in entry.items():
                        if key == '_id':
                            pass
                        elif item.get(key) == value:
                            print('Duplicate', item.get(key), '\n', value)
                            pass
                        else:
                            print('Not duplicate', item, '\n', entry)
                            # not a duplicate so we added it to the DATABASE
                            collection.insert_one(item)
            break

    # creates thread
    def start(self, item_list, receiver_ip):
        self.__listener = threading.Thread(target=self.connect_2db(item_list, receiver_ip))
        self.__listener.start()


receiver_ip = 'localhost'
sync_sender = Sender()
item_list = []
sync_sender.start(item_list, receiver_ip)
