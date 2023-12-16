from flask import render_template, current_app as app, request
from flask_security import auth_required, roles_required, current_user
from ..controller import editCartItem, deleteCartItem, getUserCartItems, createCartItem, getCart, getCartItem, getProduct, getProductAvailableQuantity
from ..utils import request_error, request_ok, marshal_cart_items

@app.route('/cart', methods=['GET'])
@auth_required('token')
@roles_required("user")
def user_cart():
    cart_items = getUserCartItems(uid=current_user.id)

    if cart_items is not None:
        payload = marshal_cart_items(cart_items)

        return request_ok(payload=payload)
    else: 
        return request_error()

@app.route('/cart/item/remove/<id>', methods=['POST'])
@auth_required('token')
@roles_required("user")
def user_cart_item_remove(id):
    data = request.get_json()

    quantity = int(data.get('quantity'))

    cart_item = getCartItem(id)

    if quantity == cart_item.quantity:
        deleted = deleteCartItem(cart_item.id)

        if deleted:
            return request_ok(message="Item removed from cart.")
    elif quantity < cart_item.quantity:
        _q = cart_item.quantity - quantity

        editData = {
            'id': cart_item.id,
            "quantity": _q
        }

        edited = editCartItem(editData)

        if edited:
            return request_ok(message="Item edited.")
    else:
        return request_error("Incorrect input value.")
    
    

@app.route('/cart/item/add/<id>', methods=['POST'])
@auth_required('token')
@roles_required("user")
def user_cart_item_add(id):

    data = request.get_json()

    if (id == "new"):
        cart = getCart(uid=current_user.id)
        product = getProduct(id=data.get('product'))
        quantity = int(data.get('quantity'))

        a_quantity = getProductAvailableQuantity(product.id)

        if quantity > a_quantity:
            return request_error("Incorrect quantity amount")
        
        createData = {
            'product': product.id,
            'cart': cart.id,
            'quantity': quantity,
        }

        cart_item = createCartItem(createData)

        if cart_item:
            return request_ok(message="Added item to cart")
        else:
            return request_error()
        
    elif id.isnumeric():
        cart_item = getCartItem(id)
        quantity_ = data.get('quantity')

        quantity = int(quantity_ if quantity_ else 1)

        f_quantity = int(cart_item.quantity) + quantity

        a_quantity = getProductAvailableQuantity(cart_item.product)

        if f_quantity > a_quantity:
            return request_error("Incorrect quantity amount")
        
        editData = {
            'id': id,
            'quantity': f_quantity
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