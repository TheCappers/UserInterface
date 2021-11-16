from pymongo import MongoClient
from bson.objectid import ObjectId


class DataBase:

    def __init__(self):
        db_server_url = 'mongodb://localhost:27017/'
        client = MongoClient(db_server_url)
        self.db = client['AVERT']
        self.keystroke_collection = self.db["keystroke_collection"]
        self.mouse_collection = self.db["mouse_collection"]
        self.screenshot_collection = self.db["screenshot_collection"]
        self.process_collection = self.db["process_collection"]
        self.windows_collection = self.db["windows_collection"]
        self.syscall_collection = self.db["syscall_collection"]
        self.video_collection = self.db["video_collection"]
        self.network_collection = self.db["network_collection"]

    def __insert_post(self, collection, post):
        # print(post.get("_id"), post.get("name"))
        try:
            temp = collection.find({"_id": post.get("_id")})[0]
        except Exception:
            post.update({"_id": ObjectId().__str__()})
            # print(post)
            collection.insert_one(post)
            pass

    # returns list based on the searched post in all... Will be reworked for multiple filters
    def __find(self, target):
        db_list = []
        for data_type in self.db.list_collection_names():
            for entry in self.db[data_type].find():
                for key, value in entry.items():
                    if type(value) == dict:
                        if target in value.values():
                            db_list.append(entry)
                            # print(entry)
                    elif target in value:
                        # print(entry)
                        db_list.append(entry)
        return db_list

    # returns list of everything based on that type.
    def __get_type(self, collection):
        db_list = []
        for entry in collection.find({}):
            db_list.append(entry)
        return db_list

    # return a list of items in the database.
    def __get_all(self):
        db_list = []
        for data_type in self.db.list_collection_names():
            for entry in self.db[data_type].find({}):
                db_list.append(entry)
        return db_list

    # updated an item based on unique id
    def __update_one(self, collection, post, updated_post):
        collection.update_one({"_id": post.get("_id")}, {"$set": updated_post})

    # deletes an item based on unique id
    def __delete_one(self, collection, post):
        collection.delete_one({"_id": post.get("_id")})

    def query_db(self, query, post, target):
        # returns a list of all items on the database
        if query == "all":
            return self.__get_all()

        # returns list of data based on everything that has been filtered
        if query == "find":
            return self.__find(target)

        if query == "post":
            if post.get('name') == "Keystroke":
                self.__insert_post(self.keystroke_collection, post)
            if post.get('name') == "Mouse_Action":
                self.__insert_post(self.mouse_collection, post)
            if post.get('name') == "Screenshot":
                self.__insert_post(self.screenshot_collection, post)
            if post.get('name') == "Process":
                self.__insert_post(self.process_collection, post)
            if post.get('name') == "Window_History":
                self.__insert_post(self.windows_collection, post)
            if post.get('name') == "System_Call":
                self.__insert_post(self.syscall_collection, post)
            if post.get('name') == "Video":
                self.__insert_post(self.video_collection, post)
            if post.get('name') == "Network":
                self.__insert_post(self.network_collection, post)

        # returns a list all based on data type e.g. Keystroke or Mouse_Action
        if query == "get_type":
            if target == "Keystroke":
                return self.__get_type(self.keystroke_collection)
            if target == "Mouse_Action":
                return self.__get_type(self.mouse_collection)
            if target == "Screenshot":
                return self.__get_type(self.screenshot_collection)
            if target == "Process":
                return self.__get_type(self.process_collection)
            if target == "Window_History":
                return self.__get_type(self.windows_collection)
            if target == "System_Call":
                return self.__get_type(self.syscall_collection)
            if target == "Video":
                return self.__get_type(self.video_collection)
            if target == "Network":
                return self.__get_type(self.network_collection)

        if query == "update":
            if post.get('name') == "Keystroke":
                self.__update_one(self.keystroke_collection, post, target)
            if post.get('name') == "Mouse_Action":
                self.__update_one(self.mouse_collection, post, target)
            if post.get('name') == "Screenshot":
                self.__update_one(self.screenshot_collection, post, target)
            if post.get('name') == "Process":
                self.__update_one(self.process_collection, post, target)
            if post.get('name') == "Window_History":
                self.__update_one(self.windows_collection, post, target)
            if post.get('name') == "System_Call":
                self.__update_one(self.syscall_collection, post, target)
            if post.get('name') == "Video":
                self.__update_one(self.video_collection, post, target)
            if post.get('name') == "Network":
                self.__update_one(self.network_collection, post, target)

        if query == "delete":
            if post.get('name') == "Keystroke":
                self.__delete_one(self.keystroke_collection, post)
            if post.get('name') == "Mouse_Action":
                self.__delete_one(self.mouse_collection, post)
            if post.get('name') == "Screenshot":
                self.__delete_one(self.screenshot_collection, post)
            if post.get('name') == "Process":
                self.__delete_one(self.process_collection, post)
            if post.get('name') == "Window_History":
                self.__delete_one(self.windows_collection, post)
            if post.get('name') == "System_Call":
                self.__delete_one(self.syscall_collection, post)
            if post.get('name') == "Video":
                self.__delete_one(self.video_collection, post)
            if post.get('name') == "Network":
                self.__delete_one(self.network_collection, post)

        if query == "deep_search":
            return self.__deep_search(target)

# post_1 = {'_id': '615b8dee3f96615d6166ead6', 'name': 'Mouse_Action', 'Keystroke': 'H', 'Date': '9/11/2021', 'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': 'David'}

# db = DataBase()
#
# root_list = db.query_db("find", "", "polkitd")

# for root in root_list:
#     print(root)

# insert data to the database
# db.query_db("post", post_1, "")

# return a list of all items in the database
# list_all = db.query_db("all", "", "")
# for entry in list_all:
#     print(entry)

# updates the an entry based on the updated post. Can be one or two columns
# updated_post = {"Tag": ["Manny", "Likes", "Chips"]}
# db.query_db("update", post_1, updated_post)

# find everything based on a filter e.g. Tag = Manny
# temp_list = db.query_db("find", "", {"Tag": "Manny"})
# for entry in temp_list:
#     print(entry)

# return a list of all items in the a collection from the database
# all_list = db.query_db("get_type", "", "Keystroke")
# for entry in all_list:
#     print(entry)

# deletes a selected item (Post_X) from the database
# post_x = {'_id': '615b8dee3f96615d6166ead6', 'name': 'Mouse_Action', 'Keystroke': 'H', 'Date': '9/11/2021', 'IP Address': '1.2.3.4', 'Annotation': '', 'Tag': 'David'}
# db.query_db("delete", post_x, "")
