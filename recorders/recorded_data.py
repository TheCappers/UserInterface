import socket
from uuid import getnode as get_mac
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
        self._recorded_data = {"ip_address": '', "mac_address": '', 'timestamp': '', "name": '', "data": {}}

    def get_ip_address(self):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip

    def get_mac_address(self):
        mac = get_mac()
        return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2)) 
    
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

    def save_recorded_data(self, data_dict):
        print(data_dict)
        self.recorded_data.update(data_dict)
        print(self.recorded_data)
        DataBase().db_query("post", self.recorded_data, "")
        print(data_dict)
        print(DataBase().query_db("find", self.recorded_data, "")) # for checking purpose
        return

# R = RecordedData()
# print(R.get_mac_address())
