from flask import current_app as app, request, render_template
from flask_security import auth_required, current_user
from ..utils import request_error, request_ok, request_not_found

@app.route('/', methods=['GET'])
def homepage():
    
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
@auth_required('token')
def user_search():
    data = request.get_json()

    name = data.get('name')
    filter = data.get('filter')

    
    return request_ok(message="done")