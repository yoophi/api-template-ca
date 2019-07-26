from app.request_objects import ValidRequestObject


class TodoItemRequestObject(ValidRequestObject):
    def __init__(self, id=None):
        self.id = id

    @classmethod
    def from_dict(cls, adict):
        return cls(id=adict.get('id', None))
