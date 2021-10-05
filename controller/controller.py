from configuration import configuration
from Database import Database

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

    def storageRecording(self, amount):
        self.config.setThreshold(amount)
        full = self.config.storage_alert()
        return full  # send to view

    def export(self, item):  # here is where we would use the database to export
        return

    def view(self, item):  # here is where we would connect to database to view an item in avert
        if item == '':
            data = self.db.query_db('find_all', {'name': 'Mouse_Action'}, '')
            print(data)
            #return data

        if item.lower() == 'keystrokes' or item.lower() == 'mouse action':
            data = self.db.query_db('find_all', {'name': 'Keystroke'}, '')
        else:
            data = self.db.query_db('find_all', {'name': 'Mouse_Action'}, '')
        print(data)
        #return data


    def annotationAdd(self, annot, item): # here we update the item in the DB with an annotation
        '''
        post_1 = {
            "name": "Mouse_Action",
            "Keystroke": "H",
            "Date": "9/11/2021",
            "IP Address": "1.2.3.4",
            'Annotation': []
            'Tag': []
            post_x = {
                "_id": "99",
                "name": "Keystroke",
                "Keystroke": "Manny",
                "Date": "9/11/2380923874276",
                "IP Address": "1.2.3fgfdjshakdf.4",
}
        '''
        return

    def tagAdd(self, tag, item):
        return

    def tagDelete(self, tag, item):
        return
