from celery import shared_task
import json
from httplib2 import Http
from ..controller import getRequestedCategories

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