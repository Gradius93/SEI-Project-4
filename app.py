from flask import Flask
from pony.orm import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def home():
    return 'Hello beer, my old friend', 200
