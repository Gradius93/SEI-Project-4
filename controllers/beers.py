from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Beer import Beer, BeerSchema
from lib.secure_route import secure_route

router = Blueprint(__name__, 'beers')

@router.route('/beers', methods=['GET'])
@db_session
def index():
    schema = BeerSchema(many=True)
    beers = Beer.select()
    return schema.dumps(beers)

@router.route('/beers', methods=['POST'])
@db_session
@secure_route
def create():
    schema = BeerSchema()

    try:
        data = schema.load(request.get_json())
        data['user'] = g.current_user
        beer = Beer(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation Failure', 'errors': err.messages}), 422
    return schema.dumps(beer), 201

@router.route('/beers/<int:beer_id>', methods=['GET'])
@db_session
def show(beer_id):
    schema = BeerSchema()
    beer = Beer.get(id=beer_id)

    if not beer:
        abort(404)

    return schema.dumps(beer)

@router.route('/beers/<int:beer_id>', methods=['PUT'])
@db_session
@secure_route
def update(beer_id):
    schema = BeerSchema()
    beer = Beer.get(id=beer_id)

    if not beer:
        abort(404)

    try:
        data = schema.load(request.get_json())
        beer.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation Failure', 'errors': err.message}), 422

    return schema.dumps(beer)

@router.route('/beers/<int:beer_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(beer_id):
    beer = Beer.get(id=beer_id)

    if not beer:
        abort(404)

    beer.delete()
    db.commit()

    return '', 204
