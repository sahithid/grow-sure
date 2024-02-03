from flask_restful import Resource, Api, marshal_with, fields, reqparse, request
from flask import jsonify
from werkzeug.exceptions import NotFound
from models import db
from models.shoppingSession import CartItem, cart_item_schema
from models.productModel import Product1, product_schema
from models.orderModel import OrderItem, Order, order_item_schema, order_schema
import models
from flask_jwt_extended import jwt_required
from jwt_decorators import admin_required
from sqlalchemy.exc import IntegrityError
import datetime


class OrderResource(Resource):
    @jwt_required()
    def get(self, user):
        user_orders = db.session.query(Order).filter_by(user_id=user)
        orders = order_schema.dump(user_orders, many=True)
        result = []
        for i in range(len(orders)):
            this_order = {}
            order_id = orders[i]['id']
            total = orders[i]['total'] 
            time = orders[i]['created_at'][:16]
            this_order['order_id'] = order_id
            this_order['total'] = total
            this_order['time'] = time
            items_ = db.session.query(OrderItem).filter_by(order_id=order_id)
            items = order_item_schema.dump(items_,many=True)
            items_ = []
            for i in range(len(items)):
                product = db.session.query(Product1).get(items[i]['product_id'])
                p = product_schema.dump(product)
                p['amount_to_buy'] = items[i]['quantity']
                items_.append(p)
            this_order['items'] = items_
            result.append(this_order)
        return result

        return jsonify({"msg": "this is the get method"})
    @jwt_required()
    def post(self, user):
        inp = request.get_json()
        current_cart = db.session.query(CartItem).filter_by(user_id=user)
        cart = cart_item_schema.dump(current_cart, many=True)
        total_ = inp["total"]
        new_order = Order(
            user_id=user, total=total_, created_at=datetime.datetime.now()
        )
        db.session.add(new_order)
        db.session.commit()
        for i in range(len(cart)):
            p_id = cart[i]["product_id"]
            bought = cart[i]["quantity"]
            product = db.session.query(Product1).get(p_id)
            if product.stock >= int(bought) : 
                new_order_item = OrderItem(
                    order_id=new_order.id,
                    quantity=int(bought),
                    product_id=p_id,
                )
                product.sold = product.sold + int(bought)
                product.stock = product.stock - int(bought)
                db.session.add(new_order_item)
                db.session.commit()
            else: 
                return jsonify({'msg':'Not enough stock! Please lower the quantity'})
        return jsonify({'msg':'Order Placed!'})

    def put(self):
        return jsonify({"msg": "this is the put method"})

    def delete(self):
        return jsonify({"msg": "this is the delete method"})
