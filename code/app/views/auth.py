from flask import current_app as app, request
from flask_security.utils import hash_password, verify_password, logout_user
from ..utils import request_error, request_ok, datastore, request_not_found, user_marshal, roles_marshal, db
from ..models import Role

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email:
        return request_error(message="Email is required")
    
    if not password:
        return request_error(message="Password is required")
    
    user = datastore.find_user(email=email)

    if not user:
        return request_not_found("No user with these credentials.")
    
    if verify_password(password, user.password):
        
        payload = user_marshal(user)
        payload['token'] = user.get_auth_token()

        return request_ok(message="User authorized.", payload=payload)
    else:
        return request_error("Wrong password")

@app.route('/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = hash_password(data.get('password'))
    role = data.get('role')

    user = datastore.create_user(email=email, password=password)
    user.name = name
    added_role = datastore.add_role_to_user(user=user, role=Role.query.get(role))
    db.session.commit()
    
    if added_role:
        payload = user_marshal(datastore.find_user(id=user.id))
        payload['token'] = user.get_auth_token()

        return request_ok(message="User signed up.", payload=payload)

@app.route('/auth/user_types', methods=['GET'])
def get_user_types():

    roles = Role.query.all()

    payload = roles_marshal(roles)
    
    payload = [d for d in payload if d.get('name') != 'admin']

    return request_ok(message="Fetched user types.", payload=payload)

@app.route('/auth/logout', methods=['GET'])
def logout():
    logout_user()
    return request_ok(message='User logged out.')