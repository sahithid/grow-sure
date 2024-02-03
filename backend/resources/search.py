from flask_restful import Resource
from flask import jsonify, request
from werkzeug.exceptions import NotFound
from models import db, bcrypt
from models.userModel import User, user_schema, login_schema
from models.productModel import Product1, product_schema
from models.categoryModel import Category1
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from jwt_decorators import admin_required


class Search(Resource):
    def post(self):
        inp = request.get_json()
        model = globals()[inp['comp']]
        if inp["search"] != "":
            search_value = "%" + inp["search"] + "%"
            column_names = model.__table__.columns.keys()

            results = []
            for i in range(len(column_names)):
                col = column_names[i]
                res = db.session.query(model).filter(
                    getattr(model, col).ilike(search_value)
                ).all()
                col_results = product_schema.dump(res, many=True)
                results = results + col_results
            return results
        else: 
            return jsonify({'msg':'Search bar cannot be empty!'})
