import os
from abc import ABC

import click
import json
import tabulate

from app import create_app
from app.request_objects.todo_list import TodoListRequestObject
from app.response_objects import ResponseSuccess
from app.use_cases.todo_list import TodoListUseCase

app = application = create_app(os.environ.get('FLASK_CONFIG') or 'default')


@app.cli.command(help='Print Todo list.')
@click.option(
    '--format',
    default='table',
    help='Output format: table, json, csv (default: table)',
)
def todos(format):
    request_object = TodoListRequestObject()
    use_case = TodoListUseCase()
    res = use_case.execute(request_object)
    if isinstance(res, ResponseSuccess):
        data = res.value
        data_formatters = {
            'table': TableFormatter,
            'json': JsonFormatter,
            'csv': CSVFormatter,
        }

        formatter = data_formatters.get(format.lower())(data)
        print(formatter.format())
    else:
        print('error occurred')


class Formatter(ABC):
    def __init__(self, data):
        self.data = []
        for row in data:
            self.data.append(row.to_dict())

    def format(self):
        pass


class TableFormatter(Formatter):
    def __init__(self, data):
        super().__init__(data)
        headers = None
        rows = []

        for n, row in enumerate(self.data):
            if n == 0:
                headers = row.keys()
            rows.append(row.values())

        self.headers = headers
        self.rows = rows

    def format(self):
        return tabulate.tabulate(self.rows, headers=self.headers)


class JsonFormatter(Formatter):
    def format(self):
        return json.dumps(self.data)


class CSVFormatter(Formatter):
    def __init__(self, data):
        super().__init__(data)
        rows = []

        for row in self.data:
            rows.append(row.values())

        self.rows = rows

    def format(self):
        out = []
        for row in self.rows:
            out.append(','.join(map(str, row)))

        return "\n".join(out)
