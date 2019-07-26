import json


class TodoJsonEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'id': str(o.id),
                'title': o.title,
                'is_done': o.is_done,
                'created_at': o.created_at.isoformat(),
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
