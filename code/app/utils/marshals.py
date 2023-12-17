from flask_restful import fields, marshal

UserMarshalFields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "role": fields.String(attribute=lambda x: x.roles[0].name),
    "active": fields.Boolean,
    "restricted": fields.Boolean
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

ProductMarshalFields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'category': fields.Integer,
    'category_details': fields.Nested(CategoryMarshalFields),
    'store_manager': fields.Integer,
    'store_manager_details': fields.Nested(UserMarshalFields),
    'price': fields.Integer,
    'unit_of_measurement': fields.String,
    'quantity_available': fields.Integer,
    'manufactured_on': fields.String,
    'expiry_date': fields.String,
    'added_on': fields.String,
    'active': fields.Boolean,
}

InvoiceDetailsMarshalFields = {
    "id": fields.Integer,
    "invoice": fields.Integer,
    "item": fields.Integer,
    "purchased_price": fields.Integer,
    "purchased_quantity": fields.Integer,
    "item_details": fields.Nested(ProductMarshalFields)
}

InvoiceMarshalFields = {
    "id": fields.Integer,
    "uid": fields.Integer,
    "purchase_date": fields.String,
    "purchased_items": fields.Nested(InvoiceDetailsMarshalFields)
}

CartItemDetailsMarshalFields = {
    "id": fields.Integer,
    "quantity": fields.Integer,
    "product": fields.Integer,
    "cart": fields.Integer,
    "product_details": fields.Nested(ProductMarshalFields)
}

CartDetailsMarshalFields = {
    "id": fields.Integer,
    "uid": fields.Integer,
    "cart_items": fields.Nested(CartItemDetailsMarshalFields)
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

def marshal_cart(data):
    return marshal(data, CartDetailsMarshalFields)