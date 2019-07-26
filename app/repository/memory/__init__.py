from app.domain.todo import Todo


class MemRepo:
    def __init__(self):
        self.data = [
            {
                'id': 1,
                'title': 'todo one',
                'is_done': True,
                'created_at': '2019-01-01 00:00:00',
            },
            {
                'id': 2,
                'title': 'todo two',
                'is_done': False,
                'created_at': '2019-01-02 00:00:00',
            }
        ]

    def list(self, filters=None):
        result = [Todo.from_dict(d) for d in self.data]

        return result

    def item(self, id=None):
        current_todo = None
        for todo in self.data:
            if str(todo['id']) == id:
                current_todo = todo

        if current_todo is None:
            raise Exception(f'There is no Todo with id: {id}')

        return Todo.from_dict(current_todo)
