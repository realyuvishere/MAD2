from flask import Flask, render_template

from app.utils import Configuration as Config
from app.utils import db

app = Flask(__name__)

Config.DEBUG = True

app.config.from_object(Config)
db.init_app(app=app)
app.app_context().push()

from app.views import *

@app.errorhandler(404)
def page_not_found(e):
    return render_template('_404.html'), 404

if __name__ == '__main__':
    app.run()