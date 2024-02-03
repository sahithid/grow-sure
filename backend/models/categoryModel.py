from models import ma,Base
from sqlalchemy import Column, Integer, String, Boolean, MetaData
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
    
class Category1(Base):
    __tablename__ = "category"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    approved = Column(Boolean, nullable=False)

    def __init__(self, name, approved):  
        self.name = name
        self.approved = approved
    

class CategorySchema(ma.Schema): 
    id = fields.Int()
    name = fields.Str()
    approved = fields.Boolean()

category_schema = CategorySchema()



# class CategorySchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Category1
#         include_relationships = True
#         load_instance = True

# category_schema = CategorySchema()














#parent_id = db.Column(db.Integer, db.ForeignKey("Cateogry.id"))
#parent = db.relationship('Category', backref="Parent", lazy="dynamic", foreign_keys='Category.id')