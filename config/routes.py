from app import app
from controllers import beers, breweries, styles, auth

app.register_blueprint(beers.router)
app.register_blueprint(breweries.router)
app.register_blueprint(styles.router)
app.register_blueprint(auth.router)
