from flask import render_template, current_app as app, request, redirect, url_for
from flask_security import auth_required, roles_required
from datetime import datetime

@auth_required('token')
@roles_required("user")
@app.route('/cart', methods=['GET'])
def user_cart():
    return render_template('user_cart.html')

@auth_required('token')
@roles_required("user")
@app.route('/cart/item/delete/<id>', methods=['POST'])
def user_cart_item_delete(id):
    return render_template('user_cart_item_delete.html')

@auth_required('token')
@roles_required("user")
@app.route('/cart/item/remove/<id>', methods=['POST'])
def user_cart_item_remove(id):
    return render_template('user_cart_item_remove.html')

@auth_required('token')
@roles_required("user")
@app.route('/cart/item/add/<id>', methods=['POST'])
def user_cart_item_add(id):
    return render_template('user_cart_item_add.html')

@auth_required('token')
@roles_required("user")
@app.route('/cart/checkout', methods=['GET'])
def user_cart_checkout():
    return render_template('user_cart_checkout.html')