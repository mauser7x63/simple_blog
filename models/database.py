from sqlalchemy import create_engine, ForeginKey
from sqlachemt import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .posts import posts_table
from .users import users_table, tokens_table

engine = create_engine('sqlite:///socnet.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)