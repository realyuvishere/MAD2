from ..models import PurchasedItems
from ..utils import db

def createPurchasedItems(data={}):
    try:
        new_purchasedItems = PurchasedItems(
            invoice=data['invoice'], 
            item=data['item'], 
            item_name=data['item_name'],
            purchased_price=data['purchased_price'], 
            purchased_quantity=data['purchased_quantity']
        )
        db.session.add(new_purchasedItems)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return new_purchasedItems

def deletePurchasedItems(id=''):
    PurchasedItems.query.filter_by(id=id).delete()
    db.session.commit()
    return True

def editPurchasedItems(data={}):
    try:
        purchasedItems = getPurchasedItem(id=data['id'])
        del data['id']
        for key in data:
            setattr(purchasedItems, key, data[key])
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def getAllPurchasedItems():
    return db.session.query(PurchasedItems).all()

def getAllPurchasedItemsByProduct(id=''):
    return db.session.query(PurchasedItems).filter(PurchasedItems.item == id).all()

def getPurchasedItem(id=''):
    return db.session.query(PurchasedItems).filter((PurchasedItems.id == id)).first()