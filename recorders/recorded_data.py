import socket
from uuid import getnode as get_mac
import os
from datetime import datetime
from Database.Database import DataBase


class RecordedData(object):
    def __init__(self):
        """ Attributes """
        # self.ip_address = ""          #172.21.0.0
        # self.mac_address = ""         #AC:FF:48:00:11:00
        # self.timestamp = ""           #13:12:10 01/21/2000
        # self.name = ""                #keystroke
        # self.collection = ""          #
        """ Attributes """
        self._recorded_data = {
            "ip_address": '', "mac_address": '', 'timestamp': '', "name": '', "data": {}, "tag": [], "annotation": []}

    # noinspection PyMethodMayBeStatic
    def get_ip_address(self):
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip

    # noinspection PyMethodMayBeStatic
    def get_mac_address(self):
        mac = get_mac()
        return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

    # noinspection PyMethodMayBeStatic
    def get_timestamp(self):
        # gets computer time
        now = datetime.now()
        # dd/mm/YY H:M:S
        return now.strftime("%H:%M:%S %m/%d/%Y")
    
    def get_recorded_data(self):
        self._recorded_data['ip_address'] = self.get_ip_address()
        self._recorded_data['mac_address'] = self.get_mac_address()
        self._recorded_data['timestamp'] = self.get_timestamp()
        return self._recorded_data

    # def save_recorded_data(self, data_dict):
    #     print(data_dict)
    #     self._recorded_data.update(data_dict)
    #     print(self._recorded_data)
    #     DataBase().db_query("post", self._recorded_data, "")
    #     print(data_dict)
    #     print(DataBase().query_db("find", self._recorded_data, "")) # for checking purpose
    #     return

    # noinspection PyMethodMayBeStatic
    def insert_to_db(self, post_data):
        DataBase().query_db("post", post_data, "")


# R = RecordedData()
# print(R.get_mac_address())
