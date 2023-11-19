from ..utils import db

class Product(db.Model):
    __tablename__='Products'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    store_manager = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    unit_of_measurement = db.Column(db.String, nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)
    manufactured_on = db.Column(db.Integer, nullable=False)
    expiry_date = db.Column(db.Integer, nullable=False)
    added_on = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)