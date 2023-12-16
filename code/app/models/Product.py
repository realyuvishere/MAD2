from datetime import datetime
from ..utils import db

class Product(db.Model):
    __tablename__='Products'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('Category.id'), nullable=False)
    store_manager = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    unit_of_measurement = db.Column(db.String, nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)
    manufactured_on = db.Column(db.String, nullable=False)
    expiry_date = db.Column(db.String, nullable=False)
    added_on = db.Column(db.String, nullable=False)
    active = db.Column(db.Integer, nullable=False)
    cart_instances = db.relationship('CartItem', backref="product_details")
    
    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'description': self.description,
    #         'category': self.category.serialize(),
    #         'store_manager': self.store_manager.serialize(),
    #         'price': self.price,
    #         'unit_of_measurement': self.unit_of_measurement,
    #         'quantity_available': self.quantity_available,
    #         'manufactured_on': self.manufactured_on,
    #         'expiry_date': self.expiry_date,
    #         'added_on': self.added_on,
    #         'active': self.active,
    #     }