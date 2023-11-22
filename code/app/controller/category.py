from ..models import Category

def createCategory(data={}):
    try:
        new_category = Category(
            name=data['name'], 
            description=data['description'], 
            active=data['active'], 
            isRequest=data['isRequest']
        )
        db.session.add(new_category)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return new_category

def deleteCategory(id=''):
    Category.query.filter_by(id=id).delete()
    db.session.commit()
    return True

def editCategory(data={}):
    try:
        category = getCategory(id=data['id'])
        del data['id']
        for key in data:
            setattr(category, key, data[key])
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def getAllCategorys():
    return db.session.query(Category).all()

def getCategory( id=''):
    category = db.session.query(Category).filter((Category.id == id)).first()
    return category