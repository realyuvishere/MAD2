from flask import current_app as app, request, jsonify, render_template
from flask_security import auth_required

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
@auth_required('token')
def user_search():
    return jsonify('user_search.html')