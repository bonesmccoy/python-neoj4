from app import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(10))
    password = Column(String(10))
