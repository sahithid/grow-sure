from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.pool import NullPool

engine = create_engine('sqlite:///store.db',poolclass=NullPool)
session_factory = sessionmaker(bind=engine,autocommit=False,autoflush=False)
session = scoped_session(session_factory)

