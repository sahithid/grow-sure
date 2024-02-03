from models import ma, Base
from marshmallow import fields
from sqlalchemy import Column, Integer, String, Boolean, MetaData, ForeignKey, Float


class Product1(Base): 
    __tablename__ = "product"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    category = Column(String, ForeignKey("category.name"), nullable=False)
    stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    manufacture_date = Column(String)
    expiry_date = Column(String)
    quantity = Column(Integer)
    units = Column(String)
    sold = Column(Integer)

    def __init__(self, name, cat, stock, price, man, exp, quant, units, sold): 
        self.name = name
        self.category = cat
        self.stock = stock 
        self.price = price 
        self.manufacture_date = man
        self.expiry_date = exp
        self.quantity = quant
        self.units = units
        self.sold = sold

class ProductSchema(ma.Schema): 
    id = fields.Int()
    name = fields.Str()
    category = fields.Str()
    stock = fields.Int()
    price = fields.Float()
    manufacture_date = fields.Str()
    expiry_date = fields.Str()
    quantity = fields.Int()
    units = fields.Str()
    sold = fields.Int()

product_schema = ProductSchema()