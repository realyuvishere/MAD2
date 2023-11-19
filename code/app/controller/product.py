from ..models import Product

def createProduct(data={}):
    try:
        new_product = Product(
            name=data['name'], 
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
