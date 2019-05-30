from app import app
from controllers import beers, breweries, styles, auth

app.register_blueprint(beers.router, url_prefix='/api')
app.register_blueprint(breweries.router, url_prefix='/api')
app.register_blueprint(styles.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')
