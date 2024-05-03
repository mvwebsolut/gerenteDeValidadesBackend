from flask import Blueprint, request, jsonify, render_template
from datetime import datetime

from app.extensions import database
from app.schemas import CategorySchema

from app.models import Categorys

CategoryRoute = Blueprint("CategoryRoute", __name__, url_prefix="/categorys")

@CategoryRoute.route("/<id>", methods=["GET"])
def get_category(id):
    category = Categorys.query.filter_by(id=id).first()

    if not category:
        return jsonify({"error": True, "message": "Categoria não encontrada."}), 404

    category_schema = CategorySchema().dump(category)

    if "Mozilla" in str(request.user_agent):
        return render_template("category.html", category=category_schema)



    return category_schema, 200

@CategoryRoute.route('', methods=["GET"])
def get_categorys():
    try:
        category_schema = CategorySchema(many=True)
        categorys = Categorys.query.all()
        return category_schema.dump(categorys)
    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@CategoryRoute.route("/add", methods=["POST"])
def add_category():
    try:
        payload = request.json

        if Categorys.query.filter_by(name=payload['name']).first():
            raise Exception("categoria já foi cadastrada.")

        new_category = Categorys(
            name=payload['name'],
            added_att=datetime.now()
        )
        database.session.add(new_category)
        database.session.commit()

        category_schema = CategorySchema()

        return category_schema.dump(new_category)

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@CategoryRoute.route('/delete/<id>', methods=['GET'])
def delete_category(id):
    try:
        if not str(id).isdigit():
            return jsonify({"error": True, "message": "id da categoria inválido"}), 400

        category = Categorys.query.filter_by(id=id).first()
        if not category:
            raise Exception("Categoria não encontrado")

        database.session.delete(category)
        database.session.commit()

        return jsonify({"error": False, "message": f"Categoria {category.name} deletado com sucesso"}), 200

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400