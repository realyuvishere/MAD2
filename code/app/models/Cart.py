from ..utils import db

class Cart(db.Model):
    __tablename__='UserCart'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    uid = db.Column(db.Integer, nullable=True, unique=True)