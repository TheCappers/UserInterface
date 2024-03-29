from configuration import configuration
from Database import Database
from Script import script_maker
from Sync import sync, sender
from view.components import timeline
from shutil import copy
import os

'''
post_1 = {
    "name": "Mouse_Action",
    "Keystroke": "H",
    "Date": "9/11/2021",
    "IP Address": "1.2.3.4",
    export open file write and save
'''


class Controller(object):
    __instance = None

    def __new__(cls):
        if not Controller.__instance:
            Controller.__instance = object.__new__(cls)
        return Controller.__instance

    def __init__(self):
        self.__config = configuration.Configuration()
        self.__db = Database.DataBase()
        self.__script_gen = script_maker.ScriptMaker()
        self.__sync_tool = sync.Sync()
        self.__sync_sender = sender.Sender()
        self.__timeline_gen = timeline.Timeline()

    def universalRecording(self, signal) -> None:  # automatically records
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

    def setScreenshotType(self,type):
        self.__config.setScreenshotType(type)

    def storageRecording(self, amount) -> None:
        self.__config.setThreshold(amount)
        full = self.__config.storage_alert()
        return full  # send to view

    # fill out with all artifact types
    def syncBegin(self, exclusion, ip, tab3_widget, cancel_signal=False):
        items = ['Keystroke', 'Screenshot', "Process", 'System_Call', 'Mouse_Action', 'Window_History', 'Network', 'Video']
        attain = []

        if exclusion.lower().__contains__('video'):  # we are excluding video
            items.remove('Video')
            for i in items:
                attain += self.__db.query_db('get_type', '', i)

        if exclusion.lower().__contains__('none'):  # including video
            # include behavior
            attain = self.__db.query_db('all', '', '')

        self.__sync_tool.start(attain, ip, tab3_widget)

    def syncStatus(self):
        return self.__sync_tool.getSyncStatus()

    def getSyncPercentage(self):
        return self.__sync_sender.getPercentageInfo()

    def getSyncComplete(self):
        return self.__sync_sender.isSyncComplete()

    '''
        Signature: def export(self, item)
        Author: Manuel Galaviz
        Purpose: Export a selected item onto the desktop directory of the terminal.
        Pre: @requires item != null;
        Post: @ensures (*\ forall int i: 0<=i && i <= db_entries.length;
                        *\ results file.write(db_entries[i]));
    '''
    def export(self, item):  # here is where we would use the database to export
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        dd_dir = desktop + "/Downloads"
        if not os.path.exists(dd_dir):
            os.makedirs(dd_dir)

        db_entries = self.__db.query_db("find", "", item)

        for entry in db_entries:
            if entry.get("name") == 'Screenshot' or entry.get("name") == 'Video':
                copy(db_entries[0].get("data").get("path"), dd_dir)
                print(db_entries[0].get("data").get("path"))
            else:
                file_name = entry.get("name") + "_" + entry.get("_id") + ".txt"
                with open(os.path.join(dd_dir, file_name), 'w') as file:
                    file.write(str(entry))
                    print(file_name)
    '''
    Signature: def view(self, item)
    Author: David Amparan
    Purpose: Attains the items from the database which match item given
    Pre: @requires (*\ True )
    Post: @ensures (data is None 
                    \*)
    '''
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

    def creation_script(self, script_items):
        self.__script_gen.script(script_items)  # creation of the script

    # assume that the return given by y
    def annotationAdd(self, annotation, item):  # here we update the item in the DB with an annotation
        old = item['annotation']  # attain the old annotation regardless if any
        old.append(annotation)
        update_post = {'annotation': old}  # create the target to update
        self.__db.query_db('update', item, update_post)

    '''
    Signature: def tagAdd(self, tag, item)
    Author: David Amparan
    Purpose: Add a new tag to the given item then update the item in the database
    to hold the new tag
    Pre: @requires (*\ item not None && len(tag)>0)
    Post: @ensures (*\ tag in item('tag') 
    \* item('tag') is List)
    '''
    def tagAdd(self, tag, item):  # adding a tag
        old = item['tag']  # the old tags
        old.append(tag)
        update_post = {'tag': old}  # create the target to update
        self.__db.query_db('update', item, update_post)  # update with database

    '''
    Signature: def tagDelete(self, tag, item)
    Author: David Amparan, Emmanuel Briones
    Purpose: Delete a tag from a given item 
    Pre: @requires (*\ item not None && len(tag)>0)
    Post: @ensures (*\ tag not in item('tag') 
    \* item('tag') is List)
    '''
    def tagDelete(self, tag, item):  # delete a tag
        old_tag_list = item['tag']
        for i in tag:
            old_tag_list.remove(i)
        update_post = {'tag': old_tag_list}
        self.__db.query_db('update', item, update_post)

    def collection_total_size(self, collection_name):
        if collection_name == 'Screenshot':
            collection = self.__db.screenshot_collection
        elif collection_name == 'Video':
            collection = self.__db.video_collection
        elif collection_name == 'Network':
            collection = self.__db.network_collection
        elif collection_name == 'Processes':
            collection = self.__db.process_collection
        elif collection_name == 'Keystroke':
            collection = self.__db.keystroke_collection
        elif collection_name == 'Mouse_Actions':
            collection = self.__db.mouse_collection
        elif collection_name == 'Window_History':
            collection = self.__db.windows_collection
        else:
            collection = self.__db.syscall_collection
        return self.__db.collection_total_size(collection)

    def graphGeneration(self, type, make_up):
        if type == 'Timeline':
            self.__timeline_gen.generateTimeline(make_up)

    def updateNetworkConfig(self, time_unit, time_value):
        self.__config.updateNetwork(time_unit, time_value)

    def updateScreenshot(self, format):
        self.__config.updateScreenshot(format)

    def updateWindowHistory(self, time_unit, time_value):
        self.__config.updateWindowHistory(time_unit, time_value)

    def deleteVideoImage(self, item, name):
        if name == 'Screenshot':
            file = item['data']['path']
            os.remove(file)
        else:
            file = item['data']['path']
            os.remove(file)

    def deleteArtifact(self, target, item):
        if item == 'Video' or item == 'Screenshot':
            print(target)
            self.deleteVideoImage(target, item)
        self.__db.query_db('delete', target, '')
