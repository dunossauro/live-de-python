from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True,
                         validate=validate.Length(min=2, max=255))
    value = fields.Float(required=True)


class CartSchema(Schema):
    id = fields.Integer(required=False)
    products = fields.Nested(ProductSchema, many=True, required=True)
    total = fields.Float(required=False)
