# schema.py
from flask_restful import fields
from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    created_at = fields.DateTime()

    def jsonify(self, *args, **kwargs):
        return self.dump(*args, **kwargs)