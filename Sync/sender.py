import os
import threading, socket


class Sender:
    def __init__(self):
        self.__listener = threading.Thread()
        self.syncing = False
        self.synced = False
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sync_data(self):
        os.system("rsync -r /root/Desktop/temp/ /root/Desktop/temp2")
        #os.system("rm -r /root/Desktop/temp")
        print("rsync DATA done")

    def create_temp(self, items_list, receiver_ip):
        desk_top = os.path.join(os.environ["HOME"], "Desktop")
        dd_dir = desk_top + "/temp"
        if not os.path.exists(dd_dir):
            os.makedirs(dd_dir)

        for item in items_list:
            file_name = item.get("_id") + ".txt"
            with open(os.path.join(dd_dir, file_name), 'w') as file:
                file.write(str(item))

        self.port_flag(receiver_ip)

    def port_flag(self, receiver_ip):
        self.syncing = True
        self.client_socket.connect((receiver_ip, 777))
        self.client_socket.sendall(b'sync_ready')
        receiver_data = self.client_socket.recv(1024)
        print(receiver_data.decode())
        while True:
            if str(receiver_data.decode()) == 'receiver_ready':
                self.sync_data()
                break

    # creates thread
    def start(self, item_list, receiver_ip):
        self.__listener = threading.Thread(target=self.create_temp(item_list, receiver_ip))
        self.__listener.start()


items_list = [
            {'_id': '6191edfc31dd401df3390277', 'ip_address': '911', 'mac_address': '0123412341234', 'timestamp': '1sdfa21', 'name': 'test', 'data': 'H', 'tag': [], 'annotation': []},
            {'_id': '6191edfc31dd401df33902e6', 'ip_address': '177', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'test', 'data': 'E', 'tag': [], 'annotation': []},
            {'_id': '6191edfc31dd401df33902e8', 'ip_address': '111', 'mac_address': '00:43:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'test', 'data': 'L', 'tag': [], 'annotation': []},
            ]

receiver_ip = 'localhost'

sync_sender = Sender()
sync_sender.start(items_list, receiver_ip)
