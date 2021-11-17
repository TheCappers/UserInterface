import os
from Database.Database import DataBase
import threading, socket
import ast
from pymongo import MongoClient


class Receiver:
    def __init__(self):
        self.__listener = threading.Thread()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.__db = DataBase()

        db_server_url = 'mongodb://localhost:27017/'
        client = MongoClient(db_server_url)
        self.db = client['AVERT']

    def create_temp(self):
        # desk_top = os.path.join(os.environ["HOME"], "Desktop")
        dd_dir = r"/PycharmProjects/UserInterface/temp2"
        if not os.path.exists(dd_dir):
            os.makedirs(dd_dir)

        for data_type in self.db.list_collection_names():
            for item in self.db[data_type].find():
                file_name = item.get("_id") + ".txt"
                with open(os.path.join(dd_dir, file_name), 'w') as file:
                    file.write(str(item))

        self.update_db()

    def update_db(self):
        directory = r"/PycharmProjects/UserInterface/temp2"
        for entry in os.scandir(directory):
            if entry.is_file():
                with open(entry.path, 'r') as file:
                    data = file.read()
                    post = ast.literal_eval(str(data))
                    self.__db.query_db("post", post, "")

        # os.system("rm -r /root/Desktop/temp2")

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

                    # Create temp files and folders for rsync
                    self.create_temp()
                    break

    # creates thread
    def start(self, receiver_ip):
        self.__listener = threading.Thread(target=self.port_flag(receiver_ip))
        self.__listener.start()


# receiver_ip = 'localhost'
# sync_sender = Receiver()
# sync_sender.start(receiver_ip)
