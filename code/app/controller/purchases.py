from ..models import Purchases as Purchase

def createPurchase(data={}):
    try:
        new_purchase = Purchase(
            name=data['name'], 
        )
        db.session.add(new_purchase)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return new_purchase

def deletePurchase(id=''):
    Purchase.query.filter_by(id=id).delete()
    db.session.commit()
    return True

def editPurchase(data={}):
    try:
        purchase = getPurchase(id=data['id'])
        del data['id']
        for key in data:
            setattr(purchase, key, data[key])
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def getAllPurchases():
    return db.session.query(Purchase).all()
