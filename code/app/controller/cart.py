from ..models import Cart

def createCart(data={}):
    try:
        new_event = Cart(
            name=data['name'], 
        )
        db.session.add(new_event)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return new_event

def deleteCart(id=''):
    Cart.query.filter_by(id=id).delete()
    db.session.commit()
    return True

def editCart(data={}):
    try:
        event = getCart(id=data['id'])
        del data['id']
        for key in data:
            setattr(event, key, data[key])
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def getAllCarts():
    return db.session.query(Cart).all()
