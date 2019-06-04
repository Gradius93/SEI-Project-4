from flask import Flask, jsonify
from pony.orm import Database
from config.environment import db_uri

app = Flask(__name__, static_folder='dist')
db = Database()

db.bind('postgres', db_uri)
# pylint: disable=W0611,C0413
from config import routes

db.generate_mapping(create_tables=True)

@app.errorhandler(404)
def not_found(_error):
    return jsonify({'message': 'Not found'}), 404
