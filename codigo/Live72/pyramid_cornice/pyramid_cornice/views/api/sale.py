from cornice import Service
from pyramid.httpexceptions import HTTPCreated
from cornice.validators import marshmallow_body_validator

from pyramid_cornice.models import Cart, Product
from pyramid_cornice.views.api.schema import CartSchema

sale = Service(name="sale", path="api/v1/sale")


@sale.post(schema=CartSchema, validators=(marshmallow_body_validator,),
           content_type='application/json')
def create_sale(request):
    cart = Cart()
    for product in request.json.get('products'):
        cart.products.append(Product(**product))
    request.dbsession.add(cart)
    request.dbsession.flush()
    schema = CartSchema()
    return HTTPCreated(json=schema.dump(cart).data)



