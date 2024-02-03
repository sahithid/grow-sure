from models import ma, bcrypt, Base
from marshmallow import fields
from sqlalchemy import Column, Integer, String, Boolean, MetaData, ForeignKey, Float

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    role = Column(String(15), nullable=False)
    approved = Column(Boolean, nullable=False)

    def __init__(self, email, password, name, role, approved):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")
        self.name = name
        self.role = role
        self.approved = approved


class UserSchema(ma.Schema):
    id = fields.Int()
    email = fields.Email()
    password = fields.Str()
    name = fields.Str()
    role = fields.Str()
    approved = fields.Bool()


user_schema = UserSchema()

class LoginSchema(ma.Schema):
    email = fields.Email()
    password = fields.Str()

login_schema = LoginSchema()
