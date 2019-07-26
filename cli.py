import tabulate

from app import create_app
from app.request_objects.todo_list import TodoListRequestObject
from app.response_objects import ResponseSuccess
from app.use_cases.todo_list import TodoListUseCase

app = create_app()
app_ctx = app.app_context()
app_ctx.push()

req = TodoListRequestObject()
use_case = TodoListUseCase()

table = []
res = use_case.execute(req)
if isinstance(res, ResponseSuccess):
    todos = res.value

    for todo in todos:
        table.append([todo.id, todo.title, todo.is_done, todo.created_at])

    print(tabulate.tabulate(table, headers=['id', 'title', 'is done?', 'created at']))
