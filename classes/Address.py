from marshmallow import Schema, fields, EXCLUDE
from .Geo import Geo

class Address(Schema):

    id = fields.Integer(allow_none=False)
    city = fields.Str(allow_none=False)
    street = fields.Str(allow_none=False)
    suite = fields.Str(allow_none=False)
    zipcode = fields.Str(allow_none=False)
    geo = fields.Nested(Geo)

    
    