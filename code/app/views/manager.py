from flask import render_template, current_app as app, request
from flask_security import auth_required, roles_required, current_user
from ..controller import createCategory, deleteProduct, getProduct, editProduct, getProductsByManager, createProduct, getActiveCategories
from ..utils import request_error, request_ok, marshal_product, marshal_category
# from datetime import datetime


# @app.route('/manager/stats', methods=['GET'])
# @auth_required('token')
# @roles_required("manager")
# def manager_stats():
#     return render_template('manager_stats.html')

@app.route('/manager/categories', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_get_active_categories():
    categories = getActiveCategories()

    if categories:
        payload = marshal_category(categories)
        return request_ok(payload=payload)
    else:
        return request_error()


@app.route('/manager/products', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_products():

    id = current_user.id

    payload = getProductsByManager(id=id)

    if payload:
        payload = marshal_product(payload)
        return request_ok(payload)
    else:
        return request_error()

@app.route('/manager/products/create', methods=['POST'])
@auth_required('token')
@roles_required("manager")
def manager_products_create():
    
    data = request.get_json()

    createData = {
        'name': data.get('name'),
        'description': data.get('description'),
        'category': data.get('category'),
        'store_manager': current_user.id,
        'price': data.get('price'),
        'unit_of_measurement': data.get('unit_of_measurement'),
        'quantity_available': data.get('quantity_available'),
        'manufactured_on': data.get('manufactured_on'),
        'expiry_date': data.get('expiry_date'),
        'active': True,
    }
    

    product = createProduct(createData)

    return request_ok(message="Product created", payload=marshal_product(product))

@app.route('/manager/products/edit/<id>', methods=['POST'])
@auth_required('token')
@roles_required("manager")
def manager_products_edit(id):

    data = request.get_json()

    editData = {
        'id': int(id),
        'name': data.get('name'),
        'description': data.get('description'),
        'category': data.get('category'),
        'store_manager': int(current_user.id),
        'price': int(data.get('price')),
        'unit_of_measurement': data.get('unit_of_measurement'),
        'quantity_available': int(data.get('quantity_available')),
        'manufactured_on': data.get('manufactured_on'),
        'expiry_date': data.get('expiry_date'),
        'active': (data.get('active')),
    }

    edited = editProduct(editData)

    if edited:
        return request_ok(message="Product edited")
    else:
        return request_error()

@app.route('/manager/products/edit/<id>/restrict', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_products_resrict(id):

    data = {
        'id': id,
        'active': False
    }

    edited = editProduct(data)
    
    if edited:
        return request_ok(message="Product restricted")
    else:
        return request_error()

@app.route('/manager/products/delete/<id>', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_products_delete(id):

    product = getProduct(id)

    if product.store_manager.id == current_user.id:
        deleteProduct(id)

        return request_ok(message="Product deleted.")
    else:
        return request_error(message="Problem while deleting.")

@app.route('/manager/category/request', methods=['POST'])
@auth_required('token')
@roles_required("manager")
def manager_category_request():
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    active = False
    isRequest = True

    categoryData = {
        'name': name,
        'description': description,
        'active': active,
        'isRequest': isRequest
    }

    createCategory(categoryData)

    return request_ok(message="Request sent successfully.")