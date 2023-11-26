from ..models import Product
from ..utils import db

def createProduct(data={}):
    try:
        new_product = Product(
            name=data['name'], 
            description=data['description'], 
            category=data['category'], 
            store_manager=data['store_manager'], 
            price=data['price'], 
            unit_of_measurement=data['unit_of_measurement'], 
            quantity_available=data['quantity_available'], 
            manufactured_on=data['manufactured_on'], 
            expiry_date=data['expiry_date'],
            added_on=data['added_on'],
            active=data['active']
        )
        db.session.add(new_product)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return new_product

def deleteProduct(id=''):
    Product.query.filter_by(id=id).delete()
    db.session.commit()
    return True

def editProduct(data={}):
    try:
        product = getProduct(id=data['id'])
        del data['id']
        for key in data:
            setattr(product, key, data[key])
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def getAllProducts():
    return db.session.query(Product).all()

def getProduct(id=''):
    product = db.session.query(Product).filter((Product.id == id)).first()

    return product