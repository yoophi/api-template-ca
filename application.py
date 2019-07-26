import os

import click
import tabulate

from app import create_app
from app.request_objects.todo_list import TodoListRequestObject
from app.response_objects import ResponseSuccess
from app.use_cases.todo_list import TodoListUseCase

app = application = create_app(os.environ.get('FLASK_CONFIG') or 'default')


@app.cli.command()
@click.option('--format', default='table',
              help='output format table / csv')
def todos(format):
    table = []
    use_case = TodoListUseCase()

    res = use_case.execute(TodoListRequestObject())
    if isinstance(res, ResponseSuccess):
        todos = res.value

        for todo in todos:
            table.append([todo.id, todo.title, todo.is_done, todo.created_at])

        if format == 'table':
            print(tabulate.tabulate(table, headers=['id', 'title', 'is done?', 'created at']))
        else:
            for row in table:
                print(','.join(map(str, row)))

    else:
        print('error occurred')
