from flask_restful import fields, marshal
from datetime import datetime

UserMarshalFields = {
    "id": fields.Integer,
    "email": fields.String,
}

def user_marshal(data):
    return marshal(data, UserMarshalFields)