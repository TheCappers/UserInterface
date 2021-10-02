import socket
from uuid import getnode as get_mac
from datetime import datetime

class RecordedData:
    def __init__(self):
        """ Attributes """
        # self.ip_address = ""          #172.21.0.0
        # self.mac_address = ""         #AC:FF:48:00:11:00
        # self.timestamp = ""           #13:12:10 01/21/2000
        # self.name = ""                #keystroke
        # self.collection = ""          #
        """ Attributes """
        self.recorded_data = {"ip_address": '', "mac_address": '', 'timestamp': '', "name": 'mouse_action', "data": {}}

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
        return self.recorded_data


R = RecordedData()
print(R.get_mac_address())