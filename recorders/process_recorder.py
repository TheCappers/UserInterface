import psutil, time, threading
from recorders.recorded_data import RecordedData
from Database.Database import DataBase


class ProcessRecorder(RecordedData):

    def __init__(self):
        RecordedData.__init__(self)
        self.__autorecording = True
        self.__process = self.get_recorded_data()
        self.__process['name'] = 'Process'
        self.__process['data'] = {}
        self.__db = DataBase()
        self.__listener = threading.Thread()

    def _process_cap(self):
        while self.__autorecording:
            for process in psutil.process_iter():
                # Start time need to be converted.
                process_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(process.create_time()))
                process_type = ""
                if not process.terminal():
                    process_type = "Background"
                else:
                    process_type = "Foreground"

                process_dictionary = {
                    "username": process.username(),
                    "p_name": process.name(),
                    "pid": process.pid,
                    "ppid": process.ppid(),
                    "cpu_usage": process.cpu_percent(),
                    "memory_usage": process.memory_percent(),
                    "num_threads": process.num_threads(),
                    "status": process.as_dict().get('status'),
                    "terminal": process.environ().get('TERM'),
                    "command": process.exe(),
                    "creation_time": process_time,
                    "process_privileges": process.uids(),
                    "process_priority": process.nice(),
                    "process_type": process_type
                    }
                self.__process['data'] = process_dictionary
                self.insert_to_db()

    # creats thread
    def start(self):
        self.__listener = threading.Thread(target=self._process_cap)
        if not self.__autorecording:
            self.__autorecording = True
        self.__listener.start()

    # destroies thread
    def stop(self):
        self.__autorecording = False
        self.__listener.join()

    def insert_to_db(self):
        self.__db.query_db("post", self.__process, "")

# Sample of start and stop
# p_recorder = ProcessRecorder()
# p_recorder.start()
# p_recorder.stop()

