from flask import render_template, current_app as app, request, redirect, url_for
from flask_security import auth_required, roles_required
from datetime import datetime

@auth_required('token')
@roles_required("admin")
@app.route('/admin', methods=['GET'])
def admin_dashboard():
    return render_template('admin_dashboard.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/stats', methods=['GET'])
def admin_stats():
    return render_template('admin_stats.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/users', methods=['GET'])
def admin_users():
    return render_template('admin_users.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/users/restrict/<id>', methods=['GET', 'POST'])
def admin_users_restrict(id):
    return render_template('admin_users_restrict.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/managers', methods=['GET'])
def admin_managers():
    return render_template('admin_managers.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/managers/restrict/<id>', methods=['GET', 'POST'])
def admin_managers_restrict(id):
    return render_template('admin_managers_restrict.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/category', methods=['GET'])
def admin_category():
    return render_template('admin_category.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/category/create', methods=['GET'])
def admin_category_create():
    return render_template('admin_category_create.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/category/edit/<id>', methods=['GET'])
def admin_category_edit(id):
    '''
    Edit a given category. Approval for a category fetches the inactive category and allows editing if necessary
    '''
    return render_template('admin_category_edit.html')

@auth_required('token')
@roles_required("admin")
@app.route('/admin/category/delete/<id>', methods=['GET', 'POST'])
def admin_category_delete(id):
    return render_template('admin_category_delete.html')
