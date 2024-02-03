from flask_restful import Resource, Api, marshal_with, fields, reqparse
from flask import jsonify, request
from werkzeug.exceptions import NotFound
from models import db
from models.productModel import Product1, product_schema
from flask_jwt_extended import jwt_required
from jwt_decorators import manager_required
from sqlalchemy.exc import IntegrityError

 
# for store managers only
class Product(Resource):
    @jwt_required()
    def get(self, p_id=None):
        if p_id == None: 
            data = db.session.query(Product1).all()
            products = product_schema.dump(data, many=True)
            return products
        else: 
            data = db.session.query(Product1).filter_by(id=p_id).first()
            product = product_schema.dump(data)
            return product

    @manager_required()
    def post(self):
        inp = request.get_json()
        input = product_schema.load(inp)
        #return input
        try:
            new_product = Product1(
                name=input["name"],
                cat=input["category"],
                stock=input["stock"],
                price=input["price"],
                man=input["manufacture_date"],
                exp=input["expiry_date"],
                quant=input["quantity"],
                units=input["units"],
                sold=0
            )
            db.session.add(new_product)
            db.session.commit()
            return jsonify({"msg": "Successfully added product!"})
        except IntegrityError:
            return jsonify({"msg": "Product already exists!"})

    @manager_required()
    def put(self, p_id):
        product = db.session.query(Product1).get(p_id)

        to_be_updated = request.get_json()
        p = product_schema.load(to_be_updated)
        product.name = p["name"]
        product.category = p["category"]
        product.stock = p["stock"]
        product.price = p["price"] 
        product.manufacture_date = p["manufacture_date"]
        product.expiry_date = p["expiry_date"]
        product.quantity = p["quantity"]
        product.units = p["units"]
        product.sold = p["sold"]

        db.session.commit()

        return jsonify({"msg": "Successfully updated product with id %d" % (p_id)})

    @manager_required() 
    def delete(self, p_id):
        product = db.session.query(Product1).filter_by(id=p_id)
        product.delete()
        db.session.commit() 
        return jsonify({"msg": "Product with id %d deleted!" % (p_id)})
