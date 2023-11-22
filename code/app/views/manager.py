from flask import render_template, current_app as app, request, redirect, url_for
from datetime import datetime

@app.route('/manager', methods=['GET'])
def manager_dashboard():
    return render_template('manager_dashboard.html')

@app.route('/manager/stats', methods=['GET'])
def manager_stats():
    return render_template('manager_stats.html')

@app.route('/manager/products', methods=['GET'])
def manager_products():
    return render_template('manager_products.html')

@app.route('/manager/products/create', methods=['POST'])
def manager_products_create():
    return render_template('manager_products_create.html')

@app.route('/manager/products/edit/<id>', methods=['POST'])
def manager_products_edit(id):
    return render_template('manager_products_edit.html')

@app.route('/manager/products/edit/<id>/restrict', methods=['GET'])
def manager_products_resrict(id):
    return render_template('manager_products_edit.html')

@app.route('/manager/products/delete/<id>', methods=['GET'])
def manager_products_delete(id):
    return render_template('manager_products_delete.html')

@app.route('/manager/category/request', methods=['POST'])
def manager_category_request():
    return render_template('manager_category_request.html')