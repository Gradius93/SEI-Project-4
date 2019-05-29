from app import db
from pony.orm import Required, Optional
from marshmallow import Schema, fields, post_load

from .Brewery import Brewery
from .Style import Style

class Beer(db.Entity):
    name = Required(str)
    brewery = Required('Brewery')
    style = Required('Style')
    hops = Optional(str)
    region = Required(str)
    abv = Required(float)
    price = Required(float)
    tasting_notes = Required(str)
    user = Required('User')

class BeerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    brewery = fields.Nested('BrewerySchema', exclude=('beers',), dump_only=True)
    style = fields.Nested('StyleSchema', exclude=('beers',), dump_only=True)
    hops = fields.Str()
    region = fields.Str(required=True)
    abv = fields.Float(required=True)
    price = fields.Float(required=True)
    tasting_notes = fields.Str(required=True)
    user = fields.Nested('UserSchema', exclude=('email', 'beers'))

    @post_load
    def load_brewery(self, data):
        data['brewery'] = Brewery.get(id=data['brewery_id'])
        del data['brewery_ids']

        return data

    @post_load
    def load_style(self, data):
        data['style'] = Style.get(id=data['style_id'])
        del data['style_id']

        return data
