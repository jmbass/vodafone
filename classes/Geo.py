from marshmallow import fields, Schema, EXCLUDE

class Geo(Schema):
    id = fields.Integer(allow_none=False)
    lat = fields.Float(allow_none=False)
    lng = fields.Float(allow_none=False)

