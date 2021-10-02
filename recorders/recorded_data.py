import socket
from uuid import getnode as get_mac
from datetime import datetime

class RecordedData:
    def __init__(self):
        self.ip_address = ""
        self.mac_address = ""
        self.timestamp = ""
        self.name = ""

    def get_ip_address(self):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(local_ip)

    def get_mac_addres(self):
        print(get_mac())
    
    def get_timestamp(self):
        # gets computer time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string) 

        
rd = RecordedData()
rd.get_ip_address()
rd.get_mac_addres()
rd.get_timestamp()