from marshmallow import Schema, fields, EXCLUDE
from .Address import Address
from .Company import Company

class User(Schema):

    def __init_(self, id):
        self.id = id

    id = fields.Integer(allow_none=False)
    name = fields.Str(required=True)
    email = fields.Str(allow_none=False)
    phone = fields.Str(allow_none=False)
    username = fields.Str(allow_none=False)
    website = fields.Str(allow_none=False)
    address = fields.Nested(Address)
    company = fields.Nested(Company)


