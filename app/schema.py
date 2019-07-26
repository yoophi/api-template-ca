from marshmallow import fields

from .extensions import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'email', 'name',
        )

    created_at = fields.DateTime(format='%Y-%m-%dT%H:%M:%S+00:00')
