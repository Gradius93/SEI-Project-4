from flask import Flask
from pony.orm import Database
from config.environment import db_uri
app = Flask(__name__)
db = Database()

db.bind('postgres', db_uri)

db.generate_mapping(create_tables=True)

@app.route('/')
def home():
    return 'Hello beer, my old friend', 200
