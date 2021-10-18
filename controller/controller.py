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
        self.config = configuration.Configuration()
        self.db = Database.DataBase()

    def universalRecording(self, signal):  # automatically records
        self.config.setUniversalOn(signal)

    def mouseActionRecording(self, signal):
        self.config.setMouseAction(signal)

    def keyboardRecording(self, signal):
        self.config.setKeystroke(signal)

    def systemCallRecording(self, signal):
        return

    def windowHistoryRecording(self, signal):
        return

    def screenshotRecording(self, signal):
        return

    def processRecording(self, signal):
        return

    def storageRecording(self, amount):
        self.config.setThreshold(amount)
        full = self.config.storage_alert()
        return full  # send to view

    def export(self, item):  # here is where we would use the database to export
        desk_top = os.path.join(os.environ["HOME"], "Desktop")
        dd_dir = desk_top+"/Downloads"
        if not os.path.exists(dd_dir):
            os.makedirs(dd_dir)

        db_entries = self.db.query_db("find", "", item)
        file_name = db_entries[0].get("name") + "_" + db_entries[0].get("_id") + ".txt"
        with open(os.path.join(dd_dir, file_name), 'w') as file:
            for entry in db_entries:
                file.write(str(entry))

    def view(self, item):  # here is where we would connect to database to view an item in avert
        if item == '':
            data = self.db.query_db('all', '', '')
        elif item.lower() == 'keystrokes' or item.lower() == 'keystroke':
            data = self.db.query_db('get_type', '', 'Keystroke')  # gets the keystroke collection
        else:
            data = self.db.query_db('get_type', '', 'Mouse_Action')  # gets the mouse collection
        return data

    # assume that the return given by y
    def annotationAdd(self, annotation, item):  # here we update the item in the DB with an annotation
        old = item['annotation']  # attain the old annotation regardless if any
        old.append(annotation)
        update_post = {'annotation': old}  # create the target to update
        self.db.query_db('update', item, update_post)
        return self.db.query_db('find', '', {'_id': item['_id']})  # return the updated row

    def tagAdd(self, tag, item):  # adding a tag
        old = item['tag']  # the old tags
        old.append(tag)
        update_post = {'tag': old}  # create the target to update
        self.db.query_db('update', item, update_post)  # update with database
        return self.db.query_db('find', '', {'_id': item['_id']})

    def tagDelete(self, tag, item):  # delete a tag
        old = item['tag']
        old.remove(tag)
        update_post = {'tag': old}
        self.db.query_db('update', item, update_post)
        return self.db.query_db('find', '', {'_id': item['_id']})
