from flask_restful import Resource, Api, marshal_with, fields, reqparse, request
from flask import jsonify
from werkzeug.exceptions import NotFound
from models import db
from models.shoppingSession import CartItem, cart_item_schema
from models.productModel import Product1, product_schema
from models.orderModel import OrderItem, Order, order_item_schema, order_schema
from flask_jwt_extended import jwt_required
from jwt_decorators import admin_required
from sqlalchemy.exc import IntegrityError
import datetime


class ShoppingCartFunc(Resource):
    # show the cart
    @jwt_required()
    def get(self, user):
        cart_items = db.session.query(CartItem).filter_by(user_id = user)
        cart = cart_item_schema.dump(cart_items, many=True)
        #return len(cart)
        current_cart = []
        # return cart
        for i in range(len(cart)):
            product = db.session.query(Product1).get(cart[i]['product_id'])
            p = product_schema.dump(product)
            p['amount_to_buy'] = cart[i]['quantity']
            current_cart.append(p)
        return current_cart
        # return jsonify({'msg': 'this is the get method'})

    # add to cart
    @jwt_required()
    def post(self, user):
        inp = request.get_json()
        item = cart_item_schema.load(inp)
        current_cart = db.session.query(CartItem).filter_by(
            user_id=user, product_id = item["product_id"]
        )
        cart = cart_item_schema.dump(current_cart,many=True)
        if len(cart) == 0:
            new_item = CartItem(
                user_id=user, quantity=1, product_id=item["product_id"]
            )
            db.session.add(new_item)
            #product = db.session.query(Product1).filter_by(id = item['product_id'])
            #product.stock = product.stock - 1
            db.session.commit()

            return jsonify({'msg': 'Added to cart!'})
        else:
            return jsonify({'msg':'Already added to cart!'})

    # edit cart
    @jwt_required()
    def put(self, user, item_id):
        inp = request.get_json()
        input = cart_item_schema.load(inp)
        item_to_edit = db.session.query(CartItem).filter_by(user_id = user, product_id = item_id)
        item_to_edit.delete() 
        db.session.commit()
        new_item = CartItem(user_id = user,quantity = input['amount_to_buy'],product_id = item_id)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"msg": "this is the put method"})

    @jwt_required()
    def delete(self, user, item_id=None):
        if item_id == None:
            current_cart = db.session.query(CartItem).filter_by(user_id = user)
            current_cart.delete()
            db.session.commit()
            return jsonify({"msg": "Cart Cleared!"})
            # this is where we delete the entire cart once the user buys everything

        else:
            # this is for removing a single item from a user cart
            item_to_remove = db.session.query(CartItem).filter_by(user_id = user, product_id = item_id)
            item_to_remove.delete()
            db.session.commit()
            return jsonify({"msg": "Item removed from cart!"})
        # return jsonify({"msg": "this is the delete method"})
