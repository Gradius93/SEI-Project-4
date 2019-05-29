from app import app
from controllers import beers

app.register_blueprint(beers.router)
