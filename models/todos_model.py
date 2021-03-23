from flask import jsonify;
from models.database_model import Database

class Todo:
        
    def read(self):
        db = Database();
        
        return jsonify(
        todos=[dict(id=1, title = "Todo 1",description = "First todo in list" ,isDone = False), dict(id=2, title = "Todo 2",description = "Second todo in list" ,isDone = False)]
        )
    def save(self): 
         todo = {"title":self.title, "body": self.body}
         database = Database()
         collection = database.get_db().get_collection('todos')
         collection.insert_one(todo)
         return dict(message="OK")
    def update(self):
     return "Hello world"
    
    def set_title(self,title):
        self.title = title
    def set_body(self,body):
        self.body = body





