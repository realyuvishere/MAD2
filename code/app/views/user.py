from flask import current_app as app, request, jsonify, render_template
from flask_security import auth_required
from datetime import datetime

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@auth_required('token')
@app.route('/search', methods=['POST'])
def user_search():
    return jsonify('user_search.html')