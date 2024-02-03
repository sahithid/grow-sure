from models import ma, Base
from marshmallow import fields
from sqlalchemy import Column, Integer, String, Boolean, MetaData, ForeignKey, Float

class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    #created_at = Column(DateTime)
    #ended_at = Column(DateTime)

    def __init__(self, user_id, quantity, product_id): 
        self.user_id = user_id
        self.quantity = quantity
        self.product_id = product_id
        #self.created_at = created_at
        #self.ended_at = ended_at 


class CartItemSchema(ma.Schema): 
    id = fields.Int()
    user_id = fields.Int()
    product_id = fields.Int()
    quantity = fields.Int()
    #created_at = fields.DateTime() 
    #ended_at = fields.DateTime()

cart_item_schema = CartItemSchema()