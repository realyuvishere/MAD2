from ..utils import db
from flask_security import UserMixin, RoleMixin

class User(db.Model, UserMixin):
    __tablename__='Users'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)
    restricted = db.Column(db.Boolean(), nullable=False, default=0)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary='UserRoles', backref=db.backref('Users', lazy='dynamic'))
    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'email': self.email,
    #         'active': self.active,
    #         'restricted': self.restricted,
    #     }

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)

class UserRoles(db.Model):
    __tablename__ = 'UserRoles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('Users.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))