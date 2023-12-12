from flask import current_app as app, request
from werkzeug.security import check_password_hash
from ..utils import request_error, request_ok, datastore, request_not_found, user_marshal, roles_marshal, db
from ..models import Role
from ..controller import createUser

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
    
    if check_password_hash(user.password, password):
        
        payload = user_marshal(user)
        payload['token'] = user.get_auth_token()

        return request_ok(message="User authorized.")
    else:
        return request_error("Wrong password")

@app.route('/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    # userData = {
    #     'name': name,
    #     'email': email,
    #     'password': password,
    #     'active': True,
    #     'role': role
    # }

    # user = createUser(userData)
    user = datastore.create_user(email=email, password=password)
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

