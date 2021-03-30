import requests
import json
URL = 'http://localhost:5000/todos/'
test_data1 = {
    "title": "test todo",
    "body": "this is my test todo",
}

test_data2 = {
    "title": "  ",
    "body": "",
}

HEADERS = {
    'Content-Type': 'application/json'
}
test_data_id = " "


def test_create_todo():
    request = requests.post(URL,data=json.dumps(test_data1),headers=HEADERS)
    response = json.loads(request.content)
    global test_data_id
    test_data_id = response['id']
    assert response['message'] == "OK"

def test_create_todo_if_fields_areEmpty():
    request = requests.post(URL,data=json.dumps(test_data2),headers=HEADERS)
    response = json.loads(request.content);
    assert response['message'] == "ERROR"  #this should return an error


def test_update_todo():
    request = requests.patch(f'{URL}{test_data_id}')
    response = json.loads(request.content)
    assert response['message'] == "OK"

def test_update_todo_if_no_id():
  empty_id = " "
  request = requests.patch(f'{URL}{empty_id}')
  response = json.loads(request.content);
  assert response['message'] == "ERROR"

def test_delete_todo():
     request = requests.delete(f'{URL}{test_data_id}')
     response = json.loads(request.content);
     assert response['message'] == "OK"

def test_delete_todo_if_no_id():
  empty_id = " "
  request = requests.delete(f'{URL}{empty_id}')
  response = json.loads(request.content);
  assert response['message'] == "ERROR"


