from datetime import datetime as dt
from ..utils import db

class Purchases(db.Model):
    __tablename__='Purchases'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    purchase_date = db.Column(db.String, nullable=True, unique=True, default=dt.isoformat(dt.now()))
    purchased_items = db.relationship('PurchasedItems', backref="invoice_details")