import os
# from Database import Database
import threading, socket


class Receiver:

    def __init__(self):
        self.__listener = threading.Thread()
        self.synced = False
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # replace this with all of AVERT DATA
        self.items_list = [
            {'_id': '617f3a09acf707ca9b53e24b', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'H', 'tag': [], 'annotation': []},
            {'_id': '617f3a09acf707ca9b53e278', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'E', 'tag': [], 'annotation': []},
            {'_id': '617f3a0aacf707ca9b53e288', 'ip_address': '127.0.1.1', 'mac_address': '00:0C:29:F0:6B:3F', 'timestamp': '18:50:42 10/31/2021', 'name': 'Keystroke', 'data': 'L', 'tag': [], 'annotation': []},
            ]

    def create_temp(self, receiver_ip):
        desk_top = os.path.join(os.environ["HOME"], "Desktop")
        dd_dir = desk_top + "/temp"
        if not os.path.exists(dd_dir):
            os.makedirs(dd_dir)

        for item in self.items_list:
            file_name = item.get("_id") + ".txt"
            with open(os.path.join(dd_dir, file_name), 'w') as file:
                file.write(str(item))

        self.port_flag(receiver_ip)

    def port_flag(self, receiver_ip):
        self.client_socket.bind((receiver_ip, 777))
        self.client_socket.listen(5)
        conn, addr = self.client_socket.accept()

        with conn:
            print("Connected to: ", addr)
            while True:
                data = conn.recv(1024)
                print(data.decode())
                if str(data.decode()) == "sync_ready":
                    print("RECIVED")
                    conn.send(b'receiver_ready')
                    conn.close()
                    break

    # creates thread
    def start(self, item_list):
        self.__listener = threading.Thread(target=self.create_temp(item_list))
        self.__listener.start()


receiver_ip = 'localhost'
sync_sender = Receiver()
sync_sender.start(receiver_ip)
