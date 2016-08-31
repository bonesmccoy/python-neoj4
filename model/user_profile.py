from app import db
from sqlalchemy import Column, Integer, String, ForeignKey


class UserProfile(db.Model):
    __tablename__ = 'user_profile'

    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String(10))
    last_name = Column(String(10))
    user_id = Column(ForeignKey('user.id'), nullable=False)
