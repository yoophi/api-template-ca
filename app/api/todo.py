import json

from flask import Response

from app.api import api
from app.constants import STATUS_CODES
from app.request_objects.todo_item import TodoItemRequestObject
from app.serializer import TodoJsonEncoder
from app.use_cases.todo_item import TodoItemUseCase
from app.use_cases.todo_list import TodoListUseCase


@api.route('/v1.0/todos')
def todo_list():
    use_case = TodoListUseCase()
    response = use_case.execute()

    return Response(
        json.dumps(response.value, cls=TodoJsonEncoder),
        mimetype='application/json',
        status=STATUS_CODES[response.type]
    )


@api.route('/v1.0/todo/<id>')
def todo_item(id):
    request_object = TodoItemRequestObject.from_dict({'id': id})
    use_case = TodoItemUseCase()
    response = use_case.execute(request_object)

    return Response(
        json.dumps(response.value, cls=TodoJsonEncoder),
        mimetype='application/json',
        status=STATUS_CODES[response.type]
    )
