
class Admin:
    __tablename__='Admin'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)