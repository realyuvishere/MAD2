from ..models import Purchases as Purchase, PurchasedItems
from ..utils import db

def createPurchase(data={}):
    try:
        new_purchase = Purchase(
            uid=data['uid'], 
            purchase_date=data['purchase_date']
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

def getPurchase(id=''):
    return db.session.query(Purchase).filter((Purchase.id == id)).first()

def getPurchaseDetails(id=''):
    return db.session.query(Purchase, PurchasedItems).select_from(Purchase).join(PurchasedItems).filter((Purchase.id == id)).first()

def getUserPurchases(uid=''):
    return db.session.query(Purchase).filter((Purchase.uid == uid)).first()