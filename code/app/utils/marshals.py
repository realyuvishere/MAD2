from flask_restful import fields, marshal

UserMarshalFields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "role": fields.String(attribute=lambda x: x.roles[0].name),
}

ProductMarshalFields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'category': fields.String(attribute=lambda x: x.category[0].name),
    'store_manager': fields.String(attribute=lambda x: x.store_manager[0].name),
    'price': fields.Integer,
    'unit_of_measurement': fields.String,
    'quantity_available': fields.Integer,
    'manufactured_on': fields.String,
    'expiry_date': fields.String,
    'added_on': fields.String,
    'active': fields.Boolean,
}

RoleMarshalFields = {
    "id": fields.Integer,
    "name": fields.String,
}

CategoryMarshalFields = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    'active': fields.Boolean,
    'isRequest': fields.Boolean,
}

def marshal_roles(data):
    return marshal(data, RoleMarshalFields)

def marshal_user(data):
    return marshal(data, UserMarshalFields)

def marshal_product(data):
    return marshal(data, ProductMarshalFields)

def marshal_category(data):
    return marshal(data, CategoryMarshalFields)