from recorders.recorded_data import RecordedData
from Database.Database import DataBase
import threading
import os


class NetworkRecorder(RecordedData):

    def __init__(self):
        RecordedData.__init__(self)
        self.isAutoRecord = True
        self.pcap_list = []
        self.__network_data = self.get_recorded_data()
        self.__network_data['name'] = "Network"
        self.__network_data['tree'] = ''
        self.__network_data['raw_hex'] = ''
        self.__listener = threading.Thread()
        self.start()

    def _network_cap(self):
        # CAPTURE PACKET DATA
        while self.isAutoRecord:
            pcap = os.popen("tshark -c 1 -x -PV").read()
            pcap_list = pcap.split("\n\n")
            del pcap_list[-1]

            self.__network_data['tree'] = pcap_list[0]
            self.__network_data['raw_hex'] = pcap_list[1]

            # INSERT ONE PACKET INTO DATABASE
            self.insert_to_db(self.__network_data)

    def start(self):
        self.__listener = threading.Thread(target=self._network_cap)
        if not self.isAutoRecord:
            self.isAutoRecord = True
        self.__listener.start()

    def stop(self):
        self.isAutoRecord = False
        self.__listener.join()
