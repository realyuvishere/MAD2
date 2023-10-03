from flask import render_template, current_app as app, request, redirect, url_for
from datetime import datetime

@app.route('/admin', methods=['GET'])
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/admin/stats', methods=['GET'])
def admin_stats():
    return render_template('admin_stats.html')

@app.route('/admin/users', methods=['GET'])
def admin_users():
    return render_template('admin_users.html')

@app.route('/admin/users/restrict/<id>', methods=['GET', 'POST'])
def admin_users_restrict(id):
    return render_template('admin_users_restrict.html')

@app.route('/admin/managers', methods=['GET'])
def admin_managers():
    return render_template('admin_managers.html')

@app.route('/admin/managers/restrict/<id>', methods=['GET', 'POST'])
def admin_managers_restrict(id):
    return render_template('admin_managers_restrict.html')

@app.route('/admin/category', methods=['GET'])
def admin_category():
    return render_template('admin_category.html')

@app.route('/admin/category/create', methods=['GET'])
def admin_category_create():
    return render_template('admin_category_create.html')

@app.route('/admin/category/edit/<id>', methods=['GET'])
def admin_category_edit(id):
    '''
    Edit a given category. Approval for a category fetches the inactive category and allows editing if necessary
    '''
    return render_template('admin_category_edit.html')

@app.route('/admin/category/delete/<id>', methods=['GET', 'POST'])
def admin_category_delete(id):
    return render_template('admin_category_delete.html')
