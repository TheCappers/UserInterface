import socket
from uuid import getnode as get_mac
from datetime import datetime

class RecordedData:
    def __init__(self):
        """ Attributes """
        # self.ip_address = ""
        # self.mac_address = ""
        # self.timestamp = ""
        # self.name = ""
        """ Attributes """

    def get_ip_address(self):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip

    def get_mac_addres(self):
        return get_mac()
    
    def get_timestamp(self):
        # gets computer time
        now = datetime.now()
        # dd/mm/YY H:M:S
        return now.strftime("%H:%M:%S %m/%d/%Y")
