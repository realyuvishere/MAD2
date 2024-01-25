from celery import shared_task
import json
from httplib2 import Http
from ..controller import getRequestedCategories, getAllUsers
from ..utils import datastore, send_mail
from .reports import generate_user_monthly_report, draft_monthly_report_email
from weasyprint import HTML
from base64 import b64encode

# @shared_task(ignore_result=False)
# def create_resource_csv():
#     stud_res = [] # insert data here

#     filename="test.csv"

#     # csv_output = excel.make_response_from_query_sets(stud_res, ["topic", "description"], "csv")

#     # with open(filename, 'wb') as f:
#     #     f.write(csv_output.data)

#     return filename

@shared_task(ignore_result=True)
def daily_reminder():

    categories = getRequestedCategories()

    count = len(categories)

    if count > 0:
        webhook_url = "https://chat.googleapis.com/v1/spaces/AAAAG3BFC8k/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=wd5cV1rikXiywqfI2ZUeckdjY0__1oZ0liIWJ3knHGY"

        card_message = {
            "cards": [
                {
                    "header": {
                        "title": "",
                    },
                    "sections": [
                        {
                            "widgets": [
                                {
                                    "textParagraph": {
                                        "text": f"<b><font color=\"#008080\">Dear Admin,</font></b>"
                                    }
                                },
                                {
                                    "textParagraph": {
                                        "text": f"You have {count} new category requests, visit the admin panel to review."
                                    }
                                }
                            ]
                        }
                    ]
                },
                
            ]
        }

        message_headers = {"Content-Type": "application/json; charset=UTF-8"}

        http_obj = Http()

        response = http_obj.request(
            uri=webhook_url,
            method="POST",
            headers=message_headers,
            body=json.dumps(card_message),
        )

        if response[0].status == 200:
            return "OK"
        
        return "No pending requests."

@shared_task(ignore_result=True)
def monthly_reminder():

    user_role = datastore.find_role("user")
    
    users = getAllUsers()

    u = []

    for user in users:
        if user.has_role(user_role):
            u.append(user)

    for _u in u:
        r = generate_user_monthly_report(_u)
        pdf = HTML(string=r).write_pdf()
        encoded = f"data:application/pdf;base64,{b64encode(pdf).decode('utf-8')}"

        email_content = draft_monthly_report_email(_u, encoded)

        send_mail(_u.email, f"Monthly Activity Report | {_u.name}", email_content, pdf)


    return "done"