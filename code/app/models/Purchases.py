from ..utils import db

class Purchases(db.Model):
    __tablename__='Purchases'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    uid = db.Column(db.Integer, nullable=True, unique=True)
    purchase_date = db.Column(db.Integer, nullable=True, unique=True)