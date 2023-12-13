from flask import render_template, current_app as app, request, redirect, url_for
from flask_security import auth_required, roles_required, current_user
from ..controller import createCategory, deleteProduct, getProduct, editProduct
from ..utils import request_error, request_ok, request_not_found

# @app.route('/manager', methods=['GET'])
# @auth_required('token')
# @roles_required("manager")
# def manager_dashboard():
#     return render_template('manager_dashboard.html')

# @app.route('/manager/stats', methods=['GET'])
# @auth_required('token')
# @roles_required("manager")
# def manager_stats():
#     return render_template('manager_stats.html')

@app.route('/manager/products', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_products():

    print(current_user.id)
    return render_template('manager_products.html')

@app.route('/manager/products/create', methods=['POST'])
@auth_required('token')
@roles_required("manager")
def manager_products_create():
    return render_template('manager_products_create.html')

@app.route('/manager/products/edit/<id>', methods=['POST'])
@auth_required('token')
@roles_required("manager")
def manager_products_edit(id):
    return render_template('manager_products_edit.html')

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
        return request_error(message="Something went wrong")

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