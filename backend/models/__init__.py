from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
#from marshmallow_sqlalchemy import Marshmallow

metadata = MetaData()
Base = declarative_base(metadata=metadata)

db = SQLAlchemy(metadata=metadata)

ma = Marshmallow() 
bcrypt = Bcrypt()



