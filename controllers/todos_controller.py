from flask import Blueprint,request,jsonify
from models.todos_model import Todo;

todos_blueprint = Blueprint('todos', __name__)
todos = [];

@todos_blueprint.route('/')
def read_todos():  
 todo = Todo()
 response = todo.read()
 return jsonify(dict(todos=todos))

@todos_blueprint.route('/',methods=['POST'])
def create_todos():

    data = request.get_json(silent=True)
    title = data.get('title')
    body = data.get('body')

    todo = Todo()
    todo.set_title(title)
    todo.set_body(body)
    todo.save();
    
    todos.append({
        "id":len(todos) + 1,
        "title":title,
        "body":body
    })

    return {"message": "OK"}

    return jsonify("hello world")
