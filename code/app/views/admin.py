from flask import render_template, current_app as app, request
from flask_security import auth_required, roles_required
from ..controller import getUser, getAllCategorys, createCategory, editCategory, getCategory, deleteCategory, getAllUsers
from ..utils import datastore, db, request_ok, request_not_found, request_error, marshal_category, marshal_user
from ..models import Product

@app.route('/admin/users', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_users():
    user_role = datastore.find_role("user")
    
    users = getAllUsers()

    u = []

    for user in users:
        if user.has_role(user_role):
            u.append(user)

    return request_ok(payload=marshal_user(u))

@app.route('/admin/users/restrict/<id>', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_users_restrict(id):

    user = getUser(uid=id)

    user.restricted = 1

    db.session.commit()

    return request_ok(message="User has been restricted")

@app.route('/admin/users/unrestrict/<id>', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_users_unrestrict(id):

    user = getUser(uid=id)

    user.restricted = 0

    db.session.commit()

    return request_ok(message="User has been unrestricted")

@app.route('/admin/managers', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_managers():
    man_role = datastore.find_role("manager")
    
    users = getAllUsers()

    managers = []

    for user in users:
        if user.has_role(man_role):
            managers.append(user)

    return request_ok(payload=marshal_user(managers))

@app.route('/admin/category', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_category():
    categories = getAllCategorys()

    if categories is not None:
        payload = marshal_category(categories)
        return request_ok(payload=payload)
    else:
        return request_error()


@app.route('/admin/category/create', methods=['POST'])
@auth_required('token')
@roles_required("admin")
def admin_category_create():
    data = request.get_json()

    createData = {
        'name': data.get('name'),
        'description': data.get('description'),
        'active': data.get('active'),
        'isRequest': 0,
    }

    category = createCategory(createData)


    payload = marshal_category(category)

    return request_ok(message="Category created", payload=payload)

@app.route('/admin/category/edit/<id>', methods=['POST'])
@auth_required('token')
@roles_required("admin")
def admin_category_edit(id):

    data = request.get_json()

    editData = {
        'id': id,
        'name': data.get('name'),
        'description': data.get('description'),
        'active': data.get('active'),
        'isRequest': data.get('isRequest'),
    }

    edited = editCategory(editData)

    if edited:
        return request_ok(message="Category edited")
    else:
        return request_error()

@app.route('/admin/category/approve/<id>', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_category_request_approve(id):
    
    category = getCategory(id=id)
    
    category.active = 1
    category.isRequest = 0

    db.session.commit()
    
    return request_ok(message="Category approved")

@app.route('/admin/category/delete/<id>', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_category_delete(id):

    deleted = deleteCategory(id=id)

    if deleted:
        return request_ok(message="Category deleted")
