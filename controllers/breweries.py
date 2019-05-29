from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Brewery import Brewery, BrewerySchema
from lib.secure_route import secure_route

router = Blueprint(__name__, 'breweries')

@router.route('/breweries', methods=['GET'])
@db_session
def index():
    schema = BrewerySchema(many=True)
    breweries = Brewery.select()
    return schema.dumps(breweries)

@router.route('/breweries', methods=['POST'])
@db_session
@secure_route
def create():
    schema = BrewerySchema()

    try:
        data = schema.load(request.get_json())
        data['user'] = g.current_user
        brewery = Brewery(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation Failure', 'errors': err.messages}), 422
    return schema.dumps(brewery), 201

@router.route('/breweries/<int:brewery_id>', methods=['GET'])
@db_session
def show(brewery_id):
    schema = BrewerySchema()
    brewery = Brewery.get(id=brewery_id)

    if not brewery:
        abort(404)

    return schema.dumps(brewery)

@router.route('/breweries/<int:brewery_id>', methods=['PUT'])
@db_session
@secure_route
def update(brewery_id):
    schema = BrewerySchema()
    brewery = Brewery.get(id=brewery_id)

    if not brewery:
        abort(404)

    try:
        data = schema.load(request.get_json())
        brewery.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation Failure', 'errors': err.message}), 422

    return schema.dumps(brewery)

@router.route('/breweries/<int:brewery_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(brewery_id):
    brewery = Brewery.get(id=brewery_id)

    if not brewery:
        abort(404)

    brewery.delete()
    db.commit()

    return '', 204
