import pymongo

class Database:

    def __init__(self):
    # pymongo ConfigurationErrp: The dns response does not cotain an answer to the question: _mongodb._tcp.cluster0.wwlmp.mongodb.net. In srv
     url  = "mongodb://root:example@localhost:27090/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false"
     self.client = pymongo.MongoClient(url)
     self.db = self.client.get_database('todo-app')
    
    def get_db(self):
        return self.db