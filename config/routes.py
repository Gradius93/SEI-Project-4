import os
from app import app
from controllers import beers, breweries, styles, auth

app.register_blueprint(beers.router, url_prefix='/api')
app.register_blueprint(breweries.router, url_prefix='/api')
app.register_blueprint(styles.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')

@app.route('/', defaults={'path': ''}) # homepage
@app.route('/<path:path>') # any other path
def catch_all(path):

    if os.path.isfile('dist/' + path): # if path is a file, send it back
        return app.send_static_file(path)

    return app.send_static_file('index.html') # otherwise send bac
