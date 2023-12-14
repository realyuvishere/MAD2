from flask import render_template, current_app as app, request
from flask_security import auth_required, roles_required
from ..controller import getUser, getAllCategorys, createCategory, editCategory, getCategory, deleteCategory
from ..utils import datastore, db, request_ok, request_not_found, request_error, marshal_category, marshal_user

# @app.route('/admin', methods=['GET'])
# @auth_required('token')
# @roles_required("admin")
# def admin_dashboard():
#     return render_template('admin_dashboard.html')

# @app.route('/admin/stats', methods=['GET'])
# @auth_required('token')
# @roles_required("admin")
# def admin_stats():
#     return render_template('admin_stats.html')

@app.route('/admin/users', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_users():
    return render_template('admin_users.html')

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
    managers = datastore.find_user(roles=[man_role])

    return request_ok(payload=marshal_user(managers))

@app.route('/admin/category', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_category():
    categories = getAllCategorys()

    if categories:
        payload = marshal_category(categories)
        return request_ok(payload=payload)

@app.route('/admin/category/create', methods=['GET'])
@auth_required('token')
@roles_required("admin")
def admin_category_create():
    data = request.get_json()

    createData = {
        'name': data.get('name'),
        'description': data.get('description'),
        'active': 1,
        'isRequest': 0,
    }

    category = createCategory(createData)

    payload = marshal_category(category)

    return request_ok(message="Category created", payload=payload)

@app.route('/admin/category/edit/<id>', methods=['GET'])
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

    db.session.commit()
    
    return request_ok(message="Category approved")

@app.route('/admin/category/delete/<id>', methods=['GET', 'POST'])
@auth_required('token')
@roles_required("admin")
def admin_category_delete(id):

    deleted = deleteCategory(id=id)

    if deleted:
        return request_ok(message="Category deleted")
