from ..utils import db
from flask_security import UserMixin, RoleMixin

class User(db.Model, UserMixin):
    __tablename__='Users'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    restricted = db.Column(db.Integer, nullable=False)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.Integer, nullable=False)

class Role(db.Model, RoleMixin):
    __tablename__='Roles'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)