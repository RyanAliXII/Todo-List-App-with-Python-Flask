import pymongo

class Database:

    def __init__(self):
    # pymongo ConfigurationErrp: The dns response does not cotain an answer to the question: _mongodb._tcp.cluster0.wwlmp.mongodb.net. In srv
     url  = "mongodb+srv://Ryanali12:test@cluster0.wwlmp.mongodb.net/flask-db?retryWrites=true&w=majority"
     print(url)
     self.client = pymongo.MongoClient(url)
     self.db = self.client.get_database('flask-db')
    
    def get_db(self):
        return self.db