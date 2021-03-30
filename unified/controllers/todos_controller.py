from flask import Blueprint,request,jsonify
from models.todos_model import Todo

todos_blueprint = Blueprint('todos', __name__)

ERROR_MESSAGE = {
    "message":"ERROR"
}
SUCCESS_MESSAGE = {
    "message":"OK"
}

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

    if len(title.replace(" ","")) == 0 or len(body.replace(" ","")) == 0:
        return ERROR_MESSAGE

    todo = Todo()
    todo.set_title(title)
    todo.set_body(body)
    inserted_id = todo.save()
    return {"message": "OK", "id": inserted_id}

@todos_blueprint.route('/<id>',methods=['DELETE'])
def delete_todo(id):
    if len(id.replace(" ","")) == 0:
        return ERROR_MESSAGE
    todo = Todo()
    todo.delete(id)
    return SUCCESS_MESSAGE

@todos_blueprint.route('/<id>',methods=['PATCH'])
def update_todo(id):
    if len(id.replace(" ","")) == 0:
        return ERROR_MESSAGE
    todo = Todo()
    todo.update(id)
    return SUCCESS_MESSAGE

