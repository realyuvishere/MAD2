from ..utils import db

class CartItems(db.Model):
    __tablename__='UserCartItems'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    product = db.Column(db.Integer, nullable=True)
    cart = db.Column(db.Integer, nullable=True)
    quantity = db.Column(db.Integer, nullable=False)