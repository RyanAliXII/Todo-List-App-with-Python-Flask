from flask import jsonify;
from bson.objectid import ObjectId
from models.database_model import Database

class Todo:
        
    def read(self):
        database = Database();
        collection = database.get_db().get_collection('todos')
        results = collection.find({})
        result_list = []
        for result in results :
            todo = {
                "id": str(result.get('_id')),
                "title":result.get('title'),
                "body":result.get('body'),
                "isDone":result.get('isDone')
            }
            result_list.append(todo)

        return result_list
    def save(self): 
         todo = {"title":self.title, "body": self.body, "isDone": False}
         database = Database()
         collection = database.get_db().get_collection('todos')
         collection.insert_one(todo)
        
         return dict(message="OK")
    def delete(self,id):
        database = Database()
        collection = database.get_db().get_collection('todos')
        collection.delete_one({"_id":ObjectId(id)})
    def update(self,id):
        database = Database()
        collection = database.get_db().get_collection('todos')
        collection.update_one({"_id":ObjectId(id)},{"$set":{"isDone":True}})
    
    def set_title(self,title):
        self.title = title
    def set_body(self,body):
        self.body = body





