from app.repository import current_repo
from app.response_objects import ResponseSuccess, ResponseFailure


class TodoItemUseCase:
    def __init__(self):
        pass

    def execute(self, request_object):
        try:
            todos = current_repo.item(id=request_object.id)
            return ResponseSuccess(todos)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc))
            )
