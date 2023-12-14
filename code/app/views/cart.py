from flask import render_template, current_app as app, request, redirect, url_for
from flask_security import auth_required, roles_required, current_user
from ..controller import editCartItem, deleteCartItem, getUserCartItems, createCartItem, getCart, getCartItem, getProduct
from ..utils import request_error, request_ok, marshal_cart_items

@app.route('/cart', methods=['GET'])
@auth_required('token')
@roles_required("user")
def user_cart():
    cart_items = getUserCartItems(uid=current_user.id)

    payload = marshal_cart_items(cart_items)

    return request_ok(payload=payload)

@app.route('/cart/item/remove/<id>', methods=['POST'])
@auth_required('token')
@roles_required("user")
def user_cart_item_remove(id):
    return render_template('user_cart_item_remove.html')

@app.route('/cart/item/add/<id>', methods=['POST'])
@auth_required('token')
@roles_required("user")
def user_cart_item_add(id):

    data = request.get_json()

    if (id == "new"):
        cart = getCart(uid=current_user.id)
        product = getProduct(id=data.get('product'))

        createData = {
            'product': product.id,
            'cart': cart.id,
            'quantity': int(data.get('quantity')),
        }

        cart_item = createCartItem(createData)

        if cart_item:
            return request_ok(message="Added item to cart")
        else:
            return request_error()
        
    elif id.isnumeric():
        cart_item = getCartItem(id)

        editData = {
            'id': id,
            'quantity': int(data.get('quantity')) + int(cart_item.quantity)
        }

        

        edited = editCartItem(editData)

        if edited:
            return request_ok(message="Edited cart item")
        else:
            return request_error()
        
    else:
        return request_error("Wrong route")

@app.route('/cart/checkout', methods=['GET'])
@auth_required('token')
@roles_required("user")
def user_cart_checkout():
    return render_template('user_cart_checkout.html')