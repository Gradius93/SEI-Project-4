from pony.orm import Required, Set
from marshmallow import Schema, fields
from app import db

class User(db.Entity):
    username = Required(str, unique=True)
    email = Required(str, unique=True)
    password_hash = Required(str)
    beers = Set('beer')

class UserSchema(Schema):
    id = fields.Int(dumb_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(load_only=True)
    password_confirmation = fields.Str(load_only=True)
    beers = fields.Nested('BeerSchema', many=True, exclude=('user',))
