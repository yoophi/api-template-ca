from app.database import db
from app.domain.todo import Todo
from app.repository.sqla.models import Todo as TodoModel


class SqlaRepo:
    def __init__(self):
        pass

    @staticmethod
    def _create_todo_objects(results):
        return [
            Todo(
                id=q.id,
                title=q.title,
                is_done=q.is_done,
                created_at=q.created_at
            )
            for q in results
        ]

    def list(self, filters=None):
        session = db.session
        query = session.query(TodoModel)

        return self._create_todo_objects(query.all())
