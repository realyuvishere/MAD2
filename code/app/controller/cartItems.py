from ..models import CartItem

def createCartItem(data={}):
    try:
        new_cartItem = CartItem(
            name=data['name'], 
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
