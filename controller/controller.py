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

    def universalRecording(self, signal) -> None :  # automatically records
        self.__config.setUniversalOn(signal)

    def mouseActionRecording(self, signal) -> None:
        self.__config.setMouseAction(signal)

    def keyboardRecording(self, signal) -> None:
        self.__config.setKeystroke(signal)

    def systemCallRecording(self, signal):
        self.__config.setSystemCall(signal)

    def windowHistoryRecording(self, signal):
        self.__config.setWindowHistory(signal)

    def screenshotRecording(self, signal):
        self.__config.setScreenshot(signal)

    def videoRecording(self, signal):
        self.__config.setVideo(signal)

    def processRecording(self, signal):
        self.__config.setProcess(signal)

    def networkRecording(self, signal):
        self.__config.setNetwork(signal)

    def storageRecording(self, amount) -> None:
        self.__config.setThreshold(amount)
        full = self.__config.storage_alert()
        return full  # send to view

    def export(self, item) -> None:  # here is where we would use the database to export
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
        if item == '' or item.lower() == 'all':  # gets the 'name' collection
            data = self.__db.query_db('all', '', '')
            return data

        if item.lower() == 'keystrokes' or item.lower() == 'keystroke':
            data = self.__db.query_db('find', '', 'Keystroke')
            return data

        if item.lower() == 'Mouse Action' or item.lower() == 'mouse' or item.lower() == 'mouse action':
            data = self.__db.query_db('find', '', 'Mouse_Action')
            return data

        if item.lower() == 'process' or item.lower() == 'processes':
            data = self.__db.query_db('find', '', 'Process')
            return data

        if item.lower() == 'Window History' or item.lower() == 'window history' or item.lower() == 'window':
            data = self.__db.query_db('find', '', 'Window_History')
            return data

        if item.lower() == 'System Call' or item.lower() == 'system call':
            data = self.__db.query_db('find', '', "System_Call")
            return data

        if item.lower() == 'Screenshot' or item.lower() == 'screenshot' or item.lower() == 'screenshots':
            data = self.__db.query_db('find', '', 'Screenshot')
            return data

        if item.lower() == 'network' or item.lower() == 'networks' or item.lower() == 'packets':
            data = self.__db.query_db('find', '', 'Network')
            return data

        if item.lower() == 'video' or item.lower() == 'videos':
            data = self.__db.query_db('find', '', 'Video')
            return data

        else:  # anything else is either a date or other keyword
            data = self.__db.query_db('find', '', item)
            return data

    def view_filter(self, item):  # here is where we would connect to database to view an item in avert
        if item == '' or item.lower() == 'all':  # gets the 'name' collection
            data = self.__db.query_db('all', '', '')
            return data

        if item.lower() == 'keystrokes' or item.lower() == 'keystroke':
            data = self.__db.query_db('get_type', '', 'Keystroke')
            return data

        if item.lower() == 'Mouse Action' or item.lower() == 'mouse' or item.lower() == 'mouse action':
            data = self.__db.query_db('get_type', '', 'Mouse_Action')
            return data

        if item.lower() == 'process' or item.lower() == 'processes':
            data = self.__db.query_db('get_type', '', 'Process')
            return data

        if item.lower() == 'Window History' or item.lower() == 'window history' or item.lower() == 'window':
            data = self.__db.query_db('get_type', '', 'Window_History')
            return data

        if item.lower() == 'System Call' or item.lower() == 'system call':
            data = self.__db.query_db('get_type', '', "System_Call")
            return data

        if item.lower() == 'Screenshot' or item.lower() == 'screenshot' or item.lower() == 'screenshots':
            data = self.__db.query_db('get_type', '', 'Screenshot')
            return data

        if item.lower() == 'network' or item.lower() == 'networks' or item.lower() == 'packets':
            data = self.__db.query_db('get_type', '', 'Network')
            return data

        if item.lower() == 'video' or item.lower() == 'videos':
            data = self.__db.query_db('get_type', '', 'Video')
            return data

    def creation_script(self, selected):
        return
        # create the script with the given information

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
