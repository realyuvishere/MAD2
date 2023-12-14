from ..models import CartItem, Cart
from ..utils import db

def createCartItem(data={}):
    try:
        new_cartItem = CartItem(
            product=data['product'], 
            cart=data['cart'], 
            quantity=data['quantity']
        )
        db.session.add(new_cartItem)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return new_cartItem

def deleteCartItem(id=''):
    CartItem.query.filter_by(id=id).delete()
    db.session.commit()
    return True

def editCartItem(data={}):
    try:
        cartItem = getCartItem(id=data['id'])
        del data['id']
        for key in data:
            setattr(cartItem, key, data[key])
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def getAllCartItems():
    return db.session.query(CartItem).all()

def getCartItem(id=''):
    cartItem = db.session.query(CartItem).filter((CartItem.id == id)).first()
    return cartItem

def getUserCartItems(cart='', uid=''):
    if (uid):
        return db.session.query(CartItem, Cart).select_from(CartItem).join(Cart).filter((Cart.uid == uid)).all()
    return db.session.query(CartItem).filter((CartItem.cart == cart)).all()