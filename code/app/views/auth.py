from flask import render_template, jsonify, current_app as app, request, redirect, url_for
from datetime import datetime

@app.route('/auth/login', methods=['POST'])
def login():
    return jsonify({'message': 'okay'}), 200

@app.route('/auth/signup', methods=['POST'])
def signup():
    return render_template('user_cart_item_delete.html')

@app.route('/auth/user_types', methods=['GET'])
def get_user_types():
    return render_template('user_cart_item_delete.html')