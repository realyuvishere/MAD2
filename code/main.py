from flask import Flask, render_template
from flask_security import Security
from app.utils import FlaskConfig as Config, db, celery_init_app
from celery.schedules import crontab

app = Flask(__name__)

Config.DEBUG = True

app.config.from_object(Config)
app.security = Security(app, datastore)
db.init_app(app=app)
celery_app = celery_init_app(app)
app.app_context().push()

from app.views import *


@app.errorhandler(404)
def page_not_found(e):
    return render_template('_404.html'), 404

@celery_app.on_after_configure.connect
def send_email(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=19, minute=55, day_of_month=20),
        daily_reminder.s('narendra@email.com', 'Daily Test'),
    )

if __name__ == '__main__':
    app.run()