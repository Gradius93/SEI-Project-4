from app import db
from pony.orm import Required, Optional
from marshmallow import Schema, fields

class Beer(db.Entity):
    name = Required(str)
    brewery = Required(str)
    style = Required(str)
    hops = Optional(str)
    region = Required(str)
    abv = Required(float)
    price = Required(float)
    tasting_notes = Required(str)
    user = Required('User')

class BeerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    brewery = fields.Str(required=True)
    style = fields.Str(required=True)
    hops = fields.Str()
    region = fields.Str(required=True)
    abv = fields.Float(required=True)
    price = fields.Float(required=True)
    tasting_notes = fields.Str(required=True)
    user = fields.Nested('UserSchema', exclude=('email', 'sandwiches'))
