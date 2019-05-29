from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

class Brewery(db.Entity):
    name = Required(str)
    founded = Required(int)
    area = Required(str)
    beers = Set('Beer')
    user = Required('User')

class BrewerySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    founded = fields.Int(required=True)
    area = fields.Str(required=True)
    beers = fields.Nested('BeerSchema', many=True, exclude=('brewery', 'style'))
    user = fields.Nested('UserSchema', exclude=('email', 'breweries'))
