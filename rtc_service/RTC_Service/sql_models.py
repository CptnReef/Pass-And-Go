import uuid, random, string
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
    Enum
    )
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.ext.declarative import declarative_base
from RTC_Service.models import USER_RTC_ROOM_ROLE


Base = declarative_base()
        
class Room(Base):
    """model for room"""

    __tablename__ = 'rooms'
    __code_prefix__ = 'R___'

    # Object referencing
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(36), primary_key=False, autoincrement=False, unique=True, nullable=False)
    
    # Modifcation/Creation tracking
    created_datetime = Column(DateTime(timezone=True), default=datetime.utcnow())
    modified_datetime = Column(DateTime(timezone=True), onupdate=datetime.utcnow())

    # Active record
    active = Column(Boolean, index=True, nullable=False, default=True)

    access_token = Column(String(256), index=True, nullable=False, unique=True)


    def __init__(self, users=None):
        self.code = self.__code_prefix__ + uuid.uuid4().hex
        self.access_token = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=256))


    def as_dict(self):
        return_dict = dict()
        return_dict['code']=self.code
        return_dict['access_token']=self.access_token        
        return return_dict
