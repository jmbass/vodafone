from marshmallow import fields, Schema, EXCLUDE

class Company(Schema):
    id = fields.Int(allow_none=False)
    bs = fields.Str(allow_none=False)
    catchPhrase = fields.Str(allow_none=False)
    name = fields.Str(allow_none=False)