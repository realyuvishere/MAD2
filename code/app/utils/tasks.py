from celery import shared_task
from .models import StudyResource

@shared_task(ignore_result=False)
def create_resource_csv():
    stud_res = StudyResource.query.all()

    csv_output = excel.make_response_from_query_sets(stud_res, ["topic", "description"], "csv")
    filename="test.csv"

    with open(filename, 'wb') as f:
        f.write(csv_output.data)

    return filename
