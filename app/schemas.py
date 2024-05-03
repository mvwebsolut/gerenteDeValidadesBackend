from app.extensions import marshmallow as ma
from marshmallow import fields, pre_dump
from datetime import datetime


class ProductSchema(ma.Schema):

    class Meta:
        include_relationships = True

    id = fields.Field()
    name = fields.Field()
    lote_number = fields.Field()
    validity_date = fields.DateTime(format='%d/%m/%Y')
    categorys = fields.Method("slugify_category")
    days_until_expiration = fields.Method("calculate_days_until_expiration")
    added_att = fields.DateTime()

    def calculate_days_until_expiration(self, obj):
        today = datetime.now().date()
        validity_date = obj.validity_date.date()
        days_until_expiration = (validity_date - today).days
        return days_until_expiration

    def slugify_category(self, data):
        return data.categorys[0].name

class ProductClosedExpSchema(ma.Schema):

    id = fields.Field()
    name = fields.Field()
    lote_number = fields.Field()
    validity_date = fields.DateTime(format='%d/%m/%Y')
    days_until_expiration = fields.Method("calculate_days_until_expiration")
    categorys = fields.Method("slugify_category")
    added_att = fields.DateTime()

    def calculate_days_until_expiration(self, obj):
        today = datetime.now().date()
        validity_date = obj.validity_date.date()
        days_until_expiration = (validity_date - today).days
        return days_until_expiration

    @pre_dump(pass_many=True)
    def sort_products_by_expiration_date(self, data, many):
        return sorted(data, key=lambda x: x.validity_date)

    def slugify_category(self, data):
        return data.categorys[0].name

class ProductsLastAdded(ma.Schema):

    id = fields.Field()
    name = fields.Field()
    lote_number = fields.Field()
    validity_date = fields.DateTime(format='%d/%m/%Y')
    added_att = fields.DateTime()

    @pre_dump(pass_many=True)
    def sort_products_by_last_added_date(self, data, many):
        return sorted(data, key=lambda x: x.added_att)

class CategorySchema(ma.Schema):

    class Meta:
        include_relationships = True

    id = fields.Field()
    name = fields.Field()
    added_att = fields.DateTime(format='%d/%m/%Y')
    products = fields.Nested(ProductSchema, many=True)




