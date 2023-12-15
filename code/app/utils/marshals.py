from flask_restful import fields, marshal

UserMarshalFields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "role": fields.String(attribute=lambda x: x.roles[0].name),
    "active": fields.Boolean,
    "restricted": fields.Boolean
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
    'manufactured_on': fields.DateTime,
    'expiry_date': fields.DateTime,
    'added_on': fields.DateTime,
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

InvoiceMarshalFields = {
    "id": fields.Integer,
    "uid": fields.Integer,
    "purchase_date": fields.DateTime
}

InvoiceDetailsMarshalFields = {
    "id": fields.Integer,
    "uid": fields.Integer,
    "purchase_date": fields.DateTime
}

CartItemDetailsMarshalFields = {
    "id": fields.Integer,
    
}

def marshal_roles(data):
    return marshal(data, RoleMarshalFields)

def marshal_user(data):
    return marshal(data, UserMarshalFields)

def marshal_product(data):
    return marshal(data, ProductMarshalFields)

def marshal_category(data):
    return marshal(data, CategoryMarshalFields)

def marshal_invoice(data):
    return marshal(data, InvoiceMarshalFields)

def marshal_invoice_details(data):
    return marshal(data, InvoiceDetailsMarshalFields)

def marshal_cart_items(data):
    return marshal(data, CartItemDetailsMarshalFields)