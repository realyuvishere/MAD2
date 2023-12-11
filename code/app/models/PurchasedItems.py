from ..utils import db

class PurchasedItems(db.Model):
    __tablename__='PurchasedItems'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    invoice = db.Column(db.Integer, db.ForeignKey('Purchases.id'), nullable=True, unique=True)
    item = db.Column(db.Integer, db.ForeignKey('Products.id'), nullable=True, unique=False)
    purchased_price = db.Column(db.Integer, nullable=True, unique=False)
    purchased_quantity = db.Column(db.Integer, nullable=True, unique=False)