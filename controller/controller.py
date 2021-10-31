from configuration import configuration
from Database import Database
import os

'''
post_1 = {
    "name": "Mouse_Action",
    "Keystroke": "H",
    "Date": "9/11/2021",
    "IP Address": "1.2.3.4",
    export open file write and save
'''


class Controller:
    def __init__(self):
        self.__config = configuration.Configuration()
        self.__db = Database.DataBase()

    def universalRecording(self, signal):  # automatically records
        self.__config.setUniversalOn(signal)

    def mouseActionRecording(self, signal):
        self.__config.setMouseAction(signal)

    def keyboardRecording(self, signal):
        self.__config.setKeystroke(signal)

    def systemCallRecording(self, signal):
        self.__config.setSystemCall(signal)

    def windowHistoryRecording(self, signal):
        self.__config.setWindowHistory(signal)

    def Recording(self, signal):
        self.__config.setScreenshot(signal)

    def videoRecording(self, signal):
        self.__config.setVideo(signal)

    def processRecording(self, signal):
        self.__config.setProcess(signal)

    def videoRecording(self, signal):
        return

    def networkRecording(self, signal):
        return

    def storageRecording(self, amount):
        self.__config.setThreshold(amount)
        full = self.__config.storage_alert()
        return full  # send to view

    def export(self, item):  # here is where we would use the database to export
        desk_top = os.path.join(os.environ["HOME"], "Desktop")
        dd_dir = desk_top + "/Downloads"
        if not os.path.exists(dd_dir):
            os.makedirs(dd_dir)

        db_entries = self.__db.query_db("find", "", item)
        file_name = db_entries[0].get("name") + "_" + db_entries[0].get("_id") + ".txt"
        with open(os.path.join(dd_dir, file_name), 'w') as file:
            for entry in db_entries:
                file.write(str(entry))

    def view(self, item):  # here is where we would connect to database to view an item in avert
        print(item)
        if item == '' or item.lower() == 'all':  # gets the 'name' collection
            data = self.__db.query_db('all', '', '')
            print(True, ': All')
            return data

        if item.lower() == 'keystrokes' or item.lower() == 'keystroke':
            data = self.__db.query_db('get_type', '', 'Keystroke')
            print(True, ': keystroke')
            return data

        if item.lower() == 'Mouse Action' or item.lower() == 'mouse' or item.lower() == 'mouse action':
            data = self.__db.query_db('get_type', '', 'Mouse_Action')
            print(True, ': Mouse Action')
            return data

        if item.lower() == 'process' or item.lower() == 'processes':
            data = self.__db.query_db('get_type', '', 'Process')
            print(True, ': process')
            return data

        if item.lower() == 'Window History' or item.lower() == 'window history':
            data = self.__db.query_db('get_type', '', 'Window_History')
            print(True, ': Window History')
            return data

        if item.lower() == 'System Call' or item.lower() == 'system call':
            data = self.__db.query_db('get_type', '', 'System_Call')
            print(True, ': System Call')
            return data

        if item.lower() == 'Screenshot' or item.lower() == 'screenshot' or item.lower() == 'screenshots':
            data = self.__db.query_db('get_type', '', 'Screenshot')
            print(True, ': Screen shot')
            return data

    # assume that the return given by y
    def annotationAdd(self, annotation, item):  # here we update the item in the DB with an annotation
        old = item['annotation']  # attain the old annotation regardless if any
        old.append(annotation)
        update_post = {'annotation': old}  # create the target to update
        self.__db.query_db('update', item, update_post)
        return self.__db.query_db('find', '', {'_id': item['_id']})  # return the updated row

    def tagAdd(self, tag, item):  # adding a tag
        old = item['tag']  # the old tags
        old.append(tag)
        update_post = {'tag': old}  # create the target to update
        self.__db.query_db('update', item, update_post)  # update with database
        return self.__db.query_db('find', '', {'_id': item['_id']})

    def tagDelete(self, tag, item):  # delete a tag
        old = item['tag']
        old.remove(tag)
        update_post = {'tag': old}
        self.__db.query_db('update', item, update_post)
        return self.__db.query_db('find', '', {'_id': item['_id']})
