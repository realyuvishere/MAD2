from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def make_db(app, datastore):
    with app.app_context():
        from flask_security.utils import hash_password

        db.create_all()
        datastore.find_or_create_role(name="admin")
        datastore.find_or_create_role(name="manager")
        datastore.find_or_create_role(name="user")

        if not datastore.find_user(email="admin@admin.com"):
            admin = datastore.create_user(email="admin@admin.com", password=hash_password("admin"), roles=["admin"])
            admin.name = "Admin"
        
        db.session.commit()