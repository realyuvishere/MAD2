from flask import current_app as app, request
from ..utils import request_error, request_ok

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email:
        return request_error(message="Email is required")
    
    if not password:
        return request_error(message="Password is required")

    return request_ok(message="User authorized")

@app.route('/auth/signup', methods=['POST'])
def signup():
    return request_ok(message="User signed up.")

@app.route('/auth/user_types', methods=['GET'])
def get_user_types():
    return request_ok(message="Fetched user types.")

