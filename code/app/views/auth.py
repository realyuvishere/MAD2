from flask import current_app as app, request
from werkzeug.security import check_password_hash
from ..utils import request_error, request_ok, datastore, request_not_found, user_marshal

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
    return request_ok(message="User signed up.")

@app.route('/auth/user_types', methods=['GET'])
def get_user_types():
    return request_ok(message="Fetched user types.")

