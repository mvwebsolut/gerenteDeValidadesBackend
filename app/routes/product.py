from flask import Blueprint, request, jsonify, redirect, url_for
from datetime import datetime

from app.extensions import database
from app.utils.validators import validate_product
from app.schemas import ProductSchema

from app.models import Product, Categorys

ProductRoute = Blueprint("AddProduct", __name__, url_prefix="/products")

@ProductRoute.route('/', methods=["GET"])
def get_products():
    try:
        products_schema = ProductSchema(many=True)
        products = Product.query.all()
        return products_schema.dump(products)
    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@ProductRoute.route('/delete/<id>', methods=['GET'])
def delete_product(id):
    try:
        # payload = request.json
        #
        # product = Product.query.filter_by(id=payload['product_id']).first()

        product = Product.query.filter_by(id=id).first()

        if not product:
            raise Exception("Produto não encontrado")

        database.session.delete(product)
        database.session.commit()
        return redirect(url_for("HomeRoute.get_products"))
        # return jsonify({"error": False, "message": f"Produto {product.name} deletado com sucesso"}), 200

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@ProductRoute.route("/add", methods=["POST"])
def add_product():
    try:
        if not "Mozilla" in str(request.user_agent):
            product = request.json
            validate_product(product)

            if Product.query.filter_by(lote_number=product['lote_number']).first():
                raise Exception("produto já foi cadastrado.")

            try:
                category = Categorys.query.filter_by(name=product['category_name']).first()
                if not category:
                    category = Categorys(name=product['category_name'])
            except KeyError:
                category = Categorys.query.filter_by(name="sem categoria").first()
                if not category:
                    category = Categorys(name="sem categoria")

            new_product = Product(
                name=product['name'],
                lote_number=product['lote_number'],
                validity_date=datetime.strptime(product['validity_date'], "%d/%m/%Y")
            )
            new_product.categorys.append(category)
            database.session.add(new_product)
            database.session.commit()

        product = request.form.to_dict()
        print(product)

        if Product.query.filter_by(lote_number=product['product-lote']).first():
            raise Exception("produto já foi cadastrado.")

        try:
            if str(product['product-category']) == "":
                category = Categorys.query.filter_by(name="sem categoria").first()
                if not category:
                    category = Categorys(name="sem categoria")


            category = Categorys.query.filter_by(name=product['product-category']).first()
            if not category:
                category = Categorys(name=product['product-category'])
        except KeyError:
            category = Categorys.query.filter_by(name="sem categoria").first()
            if not category:
                category = Categorys(name="sem categoria")

        new_product = Product(
            name=product['product-name'],
            lote_number=product['product-lote'],
            validity_date=datetime.strptime(product['product-validity-date'], "%Y-%m-%d")
        )
        new_product.categorys.append(category)
        database.session.add(new_product)
        database.session.commit()

        return redirect(url_for("HomeRoute.get_products"))

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400






