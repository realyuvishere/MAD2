from datetime import datetime
from ..utils import db

class Purchases(db.Model):
    __tablename__='Purchases'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=True, unique=True)
    purchase_date = db.Column(db.DateTime, nullable=True, unique=True, default=datetime.now)
    purchased_items = db.relationship('PurchasedItems', backref="invoice_details")