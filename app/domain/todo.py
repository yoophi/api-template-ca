from datetime import datetime


class Todo:
    def __init__(self, id, title, is_done=False, created_at=None):
        if created_at is None:
            created_at = datetime.utcnow()
        elif type(created_at) is 'str':
            created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')

        self.id = id
        self.title = title
        self.is_done = is_done
        self.created_at = created_at

    @classmethod
    def from_dict(cls, adict):
        return cls(
            id=adict['id'],
            title=adict['title'],
            is_done=adict['is_done'],
            created_at=adict['created_at']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'is_done': self.is_done,
            'created_at': self.created_at
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
