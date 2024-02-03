from flask_restful import Resource, Api, marshal_with, fields, reqparse, request
from flask import jsonify
from werkzeug.exceptions import NotFound
from models import db
from models.categoryModel import Category1, category_schema
from models.productModel import Product1, product_schema
from flask_jwt_extended import jwt_required
from jwt_decorators import admin_required, manager_required
from sqlalchemy.exc import IntegrityError

#get_admin = db.session.query(User).filter_by(role="admin").first()

class Category(Resource): 
    #view all of the category 
    @jwt_required()
    def get(self, c_id=None):
        if c_id == None: 
            data = db.session.query(Category1).filter_by(approved = 1).all()
            categories = category_schema.dump(data, many=True)
            return categories
        else: 
            data = db.session.query(Category1).filter_by(id=c_id).first() 
            category = category_schema.dump(data)
            return category
        
    #create a new category 

    @admin_required()
    def post(self):
        inp = request.get_json()
        input_json = category_schema.load(inp) 
        try:
            new_cat = Category1(name = input_json['name'], approved = 1)
            db.session.add(new_cat)
            db.session.commit()
            return jsonify({'msg': 'Successfully added category!'})
        except IntegrityError:
            return jsonify({'msg': 'Category already exists!'})
    

    #update/edit category 
    @admin_required()
    def put(self, c_id):
        category = db.session.query(Category1).get(c_id)
        name = request.json['name'] 
        category.name = name 
        db.session.commit()

        return jsonify({'msg': 'Category Updated Successfully!'})
    
    #remove a category
    @admin_required()
    def delete(self, c_id): 
        category = db.session.query(Category1).get(c_id) 
        products = db.session.query(Product1).filter_by(category = category.name) 
        products.delete()
        category_ = db.session.query(Category1).filter_by(id = c_id) 
        category_.delete()
        db.session.commit() 

        return jsonify({'msg': 'Category deleted!'})

