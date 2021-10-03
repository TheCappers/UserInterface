import pymongo
from pymongo import MongoClient


class DataBase:

    def __init__(self):
        db_server_url = 'mongodb://localhost:27017/'
        client = MongoClient(db_server_url)
        db = client['AVERT']
        self.keystroke_collection = db["keystroke_collection"]
        self.mouse_collection = db["mouse_collection"]

    # done
    def __insert_post(self, collection, post):
        collection.insert_one(post)

    def __find_one(self, collection, post):
        return collection.find_one({"_id": post.get("_id")})

    def __find_all(self, collection):
        for entry in collection.find():
            print(entry)
        return collection.find()

    def __update_one(self, collection, post, updated_post):
        # db.collection.update_one({"_id": 2}, { "$set": {"name": "yes"} })
        collection.update_one({"_id": post.get("_id")}, {"$set": updated_post})

    def __delete_one(self, collection, post):
        # db.collection.delete_one({"_id": 2})
        collection.delete_one({"_id": post.get("_id")})

    def query_db(self, query, post, target):
        if query == "post":
            if post.get('name') == "Keystroke":
                self.__insert_post(self.keystroke_collection, post)
            if post.get('name') == "Mouse_Action":
                self.__insert_post(self.mouse_collection, post)

        if query == "find":
            if post.get('name') == "Keystroke":
                return self.__find_one(self.keystroke_collection, post)
            if post.get('name') == "Mouse_Action":
                return self.__find_one(self.mouse_collection, post)

        if query == "find_all":
            if post.get('name') == "Keystroke":
                return self.__find_all(self.keystroke_collection)
            if post.get('name') == "Mouse_Action":
                return self.__find_all(self.mouse_collection)

        if query == "update":
            if post.get('name') == "Keystroke":
                self.__update_one(self.keystroke_collection, post, target)
            if post.get('name') == "Mouse_Action":
                self.__update_one(self.mouse_collection, post, target)

        if query == "delete":
            if post.get('name') == "Keystroke":
                self.__delete_one(self.keystroke_collection, post)
            if post.get('name') == "Mouse_Action":
                self.__delete_one(self.mouse_collection, post)


post_1 = {
    "_id": "77",
    "name": "Mouse_Action",
    "Keystroke": "H",
    "Date": "9/11/2021",
    "IP Address": "1.2.3.4",
}
post_2 = {
    "_id": "27",
    "name": "Mouse_Action",
    "Keystroke": "H",
    "Date": "9/11/2021",
    "IP Address": "1.2.3.4",
}
post_3 = {
    "_id": "77",
    "name": "Keystroke",
    "Keystroke": "H",
    "Date": "9/11/2021",
    "IP Address": "1.2.3.4",
}

updated_post = {"name": "Keystroke"}

db = DataBase()
# db.query_db("post", post_1)
# db.query_db("post", post_2)
# db.query_db("post", post_3)

# find subject to change
print(db.query_db("find", post_1, ""))
print(db.query_db("find", post_2, ""))
print(db.query_db("find", post_3, ""))
print()
# find all subject to change
print(db.query_db("find_all", post_1, ""))
print()
print(db.query_db("find_all", post_3, ""))
print()
db.query_db("update", post_2, updated_post)
print(db.query_db("find", post_2, ""))
print()
db.query_db("delete", post_2, "")
print()
print(db.query_db("find_all", post_1, ""))
print()
print(db.query_db("find_all", post_3, ""))