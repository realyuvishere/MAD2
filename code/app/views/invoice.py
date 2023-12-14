from flask import render_template, current_app as app
from flask_security import auth_required, roles_required, current_user
from ..controller import getUserPurchases, getPurchaseDetails
from ..utils import marshal_invoice

@app.route('/invoice/all', methods=['GET'])
@auth_required('token')
@roles_required("user")
def get_all_invoices():

    invoices = getUserPurchases(uid=current_user.id)

    return render_template('manager_dashboard.html')

@app.route('/invoice/single/<id>', methods=['GET'])
@auth_required('token')
@roles_required("user")
def get_single_invoice(id):
    return render_template('manager_stats.html')