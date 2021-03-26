from flask import Blueprint,request,jsonify
from models.todos_model import Todo;

todos_blueprint = Blueprint('todos', __name__)


@todos_blueprint.route('/')
def read_todos():  
 todo = Todo()
 result = todo.read()
 return jsonify(dict(todos=result))

@todos_blueprint.route('/',methods=['POST'])
def create_todo():

    data = request.get_json(silent=True)
    title = data.get('title')
    body = data.get('body')
    todo = Todo()
    todo.set_title(title)
    todo.set_body(body)
    todo.save();
    
    return {"message": "OK"}

@todos_blueprint.route('/<id>',methods=['DELETE'])
def delete_todo(id):
    todo = Todo()
    todo.delete(id)
    return {"message":"OK"}

@todos_blueprint.route('/<id>',methods=['PATCH'])
def update_todo(id):
    todo = Todo()
    todo.update(id)
    return {"message":"OK"}

