from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def make_db(app, datastore):
    with app.app_context():
        db.create_all()
        datastore.find_or_create_role(name="admin")
        datastore.find_or_create_role(name="manager")
        datastore.find_or_create_role(name="user")
        db.session.commit()