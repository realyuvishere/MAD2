from flask import current_app as app, request, send_file, Response
from flask_security import auth_required, roles_required, current_user
from ..controller import createCategory, deleteProduct, getProduct, editProduct, getProductsByManager, createProduct, getActiveCategories, getProductAvailableQuantity
from ..utils import request_error, request_ok, marshal_product, marshal_category
from ..services import generate_manager_csv
from datetime import datetime

@app.route('/manager/download-csv', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_download_csv():

    file = generate_manager_csv(current_user)

    return send_file(file, as_attachment=True, mimetype="text/csv", download_name=f"{current_user.id}.csv")


@app.route('/manager/categories', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_get_active_categories():
    categories = getActiveCategories()

    if categories is not None:
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

    if payload is not None:
        payload = marshal_product(payload)
        
        for p in payload:
            p['units_available'] = getProductAvailableQuantity(p['id'])
        
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
        'added_on': datetime.now().isoformat(),
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

    if edited is not None:
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
    
    if edited is not None:
        return request_ok(message="Product restricted")
    else:
        return request_error()

@app.route('/manager/products/edit/<id>/unrestrict', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_products_unresrict(id):

    data = {
        'id': id,
        'active': True
    }

    edited = editProduct(data)
    
    if edited is not None:
        return request_ok(message="Product activated")
    else:
        return request_error()

@app.route('/manager/products/delete/<id>', methods=['GET'])
@auth_required('token')
@roles_required("manager")
def manager_products_delete(id):

    product = getProduct(id)

    if product.store_manager == current_user.id:
        deleted = deleteProduct(id)

        if deleted:
            return request_ok(message="Product deleted.")
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