from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Style import Style, StyleSchema
from lib.secure_route import secure_route

router = Blueprint(__name__, 'styles')

@router.route('/styles', methods=['GET'])
@db_session
def index():
    schema = StyleSchema(many=True)
    styles = Style.select()
    return schema.dumps(styles)

@router.route('/styles', methods=['POST'])
@db_session
@secure_route
def create():
    schema = StyleSchema()

    try:
        data = schema.load(request.get_json())
        data['user'] = g.current_user
        style = Style(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation Failure', 'errors': err.messages}), 422
    return schema.dumps(style), 201

@router.route('/styles/<int:style_id>', methods=['GET'])
@db_session
def show(style_id):
    schema = StyleSchema()
    style = Style.get(id=style_id)

    if not style:
        abort(404)

    return schema.dumps(style)

@router.route('/styles/<int:style_id>', methods=['PUT'])
@db_session
@secure_route
def update(style_id):
    schema = StyleSchema()
    style = Style.get(id=style_id)

    if not style:
        abort(404)

    try:
        data = schema.load(request.get_json())
        style.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation Failure', 'errors': err.message}), 422

    return schema.dumps(style)

@router.route('/styles/<int:style_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(style_id):
    style = Style.get(id=style_id)

    if not style:
        abort(404)

    style.delete()
    db.commit()

    return '', 204
