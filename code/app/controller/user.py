from ..models import User

def createUser(data={}):
    try:
        new_user = User(
            name=data['name'], 
        )
        db.session.add(new_user)
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return new_user

def deleteUser(id=''):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return True

def editUser(data={}):
    try:
        user = getUser(id=data['id'])
        del data['id']
        for key in data:
            setattr(user, key, data[key])
    except:
        db.session.rollback()
        raise Exception('DB error.')
    else:
        db.session.commit()
        return True

def getAllUsers():
    return db.session.query(User).all()
