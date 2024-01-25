from flask import render_template, current_app as app
from flask_security import auth_required, roles_required, current_user
from ..controller import getUserPurchases, getPurchaseDetails
from ..utils import marshal_invoice, request_ok, marshal_invoice_details, cache

@app.route('/invoice/all', methods=['GET'])
@auth_required('token')
@roles_required("user")
@cache.cached(timeout=30)
def get_all_invoices():

    invoices = getUserPurchases(uid=current_user.id)

    return request_ok(payload=marshal_invoice(invoices), message="Fetched all user invoices")

@app.route('/invoice/single/<id>', methods=['GET'])
@auth_required('token')
@roles_required("user")
def get_single_invoice(id):

    invoice = getPurchaseDetails(id)

    payload = marshal_invoice_details(invoice)

    return request_ok(payload=payload)