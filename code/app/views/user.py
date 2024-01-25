from flask import current_app as app, request, render_template
from flask_security import auth_required
from ..controller import getAllProducts, getProductsByName, getProductsByCategory, getProductAvailableQuantity
from ..utils import request_error, request_ok, request_not_found, marshal_product, cache

@app.route('/', methods=['GET'])
def homepage():
    
    return render_template('index.html')

@app.route('/search', methods=['POST'])
@auth_required('token')
def user_search():
    data = request.get_json()

    name = data.get('search')
    filter = data.get('filter')

    products = []

    if filter == 'product':
        products = getProductsByName(name=name)
    elif filter == 'category':
        p = getProductsByCategory(name=name)
        products = []
        for c in p:
            for _p in c.products:
                products.append(_p)
    
    payload = marshal_product(products)

    for p in payload:
        p['units_available'] = getProductAvailableQuantity(p['id'])
    
    return request_ok(payload=payload, message=f"Found {len(products)} results for {filter} named {name}")

@app.route('/marketplace', methods=['GET'])
@auth_required('token')
@cache.cached(timeout=50)
def user_marketplace():

    products = getAllProducts()

    payload = marshal_product(products)

    for p in payload:
        p['units_available'] = getProductAvailableQuantity(p['id'])

    return request_ok(payload=payload)