from datetime import datetime as dt
from ...controller import getUserPurchases, getProductsByManager, getProductAvailableQuantity
from jinja2 import Template
import os
from calendar import month_name
from tempfile import TemporaryFile
from csv import DictWriter
import io

basedir = os.path.abspath(os.path.dirname(__file__))

def generate_user_monthly_report(user):

    current_month = dt.now().month
    current_year = dt.now().year

    p = getUserPurchases(uid=user.id)

    _p = []

    for item in p:
        invoice_month = dt.fromisoformat(item.purchase_date).month
        invoice_year = dt.fromisoformat(item.purchase_date).year

        if (invoice_month == current_month) and (invoice_year == current_year):
            _p.append(item)
    

    f = open(os.path.join(basedir, "_templates/activity.html"), 'r')

    template = Template(f.read())

    return template.render(user=user, purchases=_p, month=month_name[current_month], year=current_year)

def draft_monthly_report_email(user, pdf_base64):
    f = open(os.path.join(basedir, "_templates/monthly_report_email.html"), 'r')
    template = Template(f.read())
    return template.render(pdf=pdf_base64, user=user)

def generate_manager_csv(manager):

    products = getProductsByManager(id=manager.id)

    # f = TemporaryFile("w+")

    f = io.StringIO()

    headers = ['product_name', 'description', 'quantity_available', 'quantity_supplied', 'quantity_purchased', 'unit_of_measurement', 'price', 'added_on', 'manufactured_on', 'expiry_date']

    writer = DictWriter(f, headers)

    writer.writeheader()

    for p in products:

        q_avail = getProductAvailableQuantity(id=p.id)
        q_purchased = int(p.quantity_available) - q_avail

        writer.writerow({'product_name': p.name, 'description': p.description, 'quantity_available': q_avail, 'quantity_purchased': q_purchased, 'quantity_supplied': p.quantity_available, 'unit_of_measurement': p.unit_of_measurement, 'price': p.price, 'added_on': p.added_on, 'manufactured_on': p.manufactured_on, 'expiry_date': p.expiry_date})
    
    mem = io.BytesIO()
    mem.write(f.getvalue().encode())
    mem.seek(0)
    f.close()

    return mem