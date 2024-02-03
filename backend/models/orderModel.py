from models import ma, Base
from marshmallow import fields
from sqlalchemy import Column, Integer, String, Boolean, MetaData, ForeignKey, Float

#order table 
# data is added here once buy is clicked on the shopping cart 

class Order(Base): 
    __tablename__ = "order"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    total = Column(Float, nullable=False)
    created_at = Column(String, nullable=False)

    def __init__(self, user_id, total, created_at): 
        self.user_id = user_id
        self.total = total 
        self.created_at = created_at 

class OrderSchema(ma.Schema): 
    id = fields.Int()
    user_id = fields.Int()
    total = fields.Float()
    created_at = fields.Str()

order_schema = OrderSchema()

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, order_id, quantity, product_id):  
        self.order_id = order_id
        self.quantity = quantity
        self.product_id = product_id

class OrderItemSchema(ma.Schema): 
    id = fields.Int()
    order_id = fields.Int()
    product_id = fields.Int()
    quantity = fields.Int()

order_item_schema = OrderItemSchema()