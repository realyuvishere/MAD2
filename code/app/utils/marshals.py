from flask_restful import fields, marshal

UserMarshalFields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "role": fields.String(attribute=lambda x: x.roles[0].name),
}

RoleMarshalFields = {
    "id": fields.Integer,
    "name": fields.String,
}

def roles_marshal(data):
    return marshal(data, RoleMarshalFields)

def user_marshal(data):
    return marshal(data, UserMarshalFields)