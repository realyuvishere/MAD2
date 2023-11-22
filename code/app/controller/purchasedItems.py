from ..models import PurchasedItems

def createPurchasedItems(data={}):
    try:
        new_purchasedItems = PurchasedItems(
            invoice=data['invoice'], 
            item=data['item'], 
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
        purchasedItems = getPurchasedItems(id=data['id'])
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
