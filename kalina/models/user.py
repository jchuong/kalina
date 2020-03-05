import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from kalina.db.base_class import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=False)
    is_superuser = Column(Boolean(), default=False)
    registered_on = Column(DateTime, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.hashed_password = password # TODO: Hash
        self.registered_on = datetime.datetime.now()

