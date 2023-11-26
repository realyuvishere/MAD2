from ..models import Cart
from ..utils import db

def createCart(data={}):
    try:
        new_cart = Cart(
            uid=data['uid']
        )
        db.session.add(new_cart)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return new_cart

def deleteCart(id=''):
    Cart.query.filter_by(id=id).delete()
    db.session.commit()
    return True

def editCart(data={}):
    try:
        cart = getCart(id=data['id'])
        del data['id']
        for key in data:
            setattr(cart, key, data[key])
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def getAllCarts():
    return db.session.query(Cart).all()

def getCart(uid='', id=''):
    cart = db.session.query(Cart).filter((Cart.id == id) | (Cart.uid == uid)).first()
    return cart