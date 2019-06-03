from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

class Style(db.Entity):
    name = Required(str)
    info = Required(str)
    beers = Set('Beer')

class StyleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    info = fields.Str(required=True)
    beers = fields.Nested('BeerSchema', many=True, exclude=('style',))
