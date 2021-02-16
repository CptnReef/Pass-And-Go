import uuid
from enum import Enum
from datetime import datetime, timedelta

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    BigInteger,
    Text
    )
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.ext.declarative import declarative_base

from flask_login import UserMixin

Base = declarative_base()


class User(Base, UserMixin):
    """model for users"""

    __tablename__ = 'User'
    __code_prefix__ = 'U___'

    id = Column(Integer, primary_key = True, autoincrement=True)
    code = Column(String(36), primary_key=False, autoincrement=False, unique=True, nullable=False)

    created_datetime = Column(DateTime(), default=datetime.now())
    modified_datetime = Column(DateTime(), onupdate=datetime.utcnow())

    email = Column(String(64), index=True, unique=True)
    username = Column(String(64), index=True, unique=False)
    password_hash = Column(String(128), index=True)

    def __init__(self, email, password, username):
        self.code = 'US__' + uuid.uuid4().hex  
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
