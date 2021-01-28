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


Base = declarative_base()


class User(Base):
    """model for users"""

    __tablename__ = 'User'
    __code_prefix__ = 'U___'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    code = db.Column(db.String(36), primary_key=False, autoincrement=False, unique=True, nullable=False)

    created_datetime = db.Column(db.DateTime(), default=datetime.now())
    modified_datetime = db.Column(db.DateTime(), onupdate=datetime.utcnow())

    email = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=False)

    password_hash = db.Column(db.String(128), index=True)

    def __init__(self, email, password, name):
        self.code = 'US__' + uuid.uuid4().hex  
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
