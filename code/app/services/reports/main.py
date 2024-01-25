from datetime import datetime as dt
from ...controller.purchases import getUserPurchases
from jinja2 import Template
import os
from calendar import month_name

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