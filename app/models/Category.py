

class Category(db.Model):
    __tablename__='Category'
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    active = db.Column(db.Integer, nullable=False) 