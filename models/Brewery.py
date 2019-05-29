from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

class Brewery(db.Entity):
    name = Required(str)
    beers = Set('Beer')

class BrewerySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    beers = fields.Nested('BeerSchema', many=True, exclude=('brewery', 'style'))
