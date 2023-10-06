from flask import render_template, current_app as app, request, redirect, url_for
from datetime import datetime

@app.route('/cart', methods=['GET'])
def user_cart():
    return render_template('user_cart.html')

@app.route('/cart/item/delete/<id>', methods=['POST'])
def user_cart_item_delete(id):
    return render_template('user_cart_item_delete.html')

@app.route('/cart/item/remove/<id>', methods=['POST'])
def user_cart_item_remove(id):
    return render_template('user_cart_item_remove.html')

@app.route('/cart/item/add/<id>', methods=['POST'])
def user_cart_item_add(id):
    return render_template('user_cart_item_add.html')

@app.route('/cart/checkout', methods=['GET'])
def user_cart_checkout():
    return render_template('user_cart_checkout.html')