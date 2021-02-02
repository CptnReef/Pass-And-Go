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

class User_RTC_Room_Association(Base):
    """ 
    model for relating user to room and holding their role
    
    """

    __tablename__ = 'user_rtc_room_associations'
    __code_prefix__ = 'UR__'

    # Object referencing
    code = Column(String(36), primary_key=False, autoincrement=False, unique=True, nullable=False)
    
    # Modifcation/Creation tracking
    created_datetime = Column(DateTime(timezone=True), default=datetime.utcnow())
    modified_datetime = Column(DateTime(timezone=True), onupdate=datetime.utcnow()) 

    user_id = Column(Integer, ForeignKey('user_rtcs.id'), primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'), primary_key=True)
    user = relationship('User_RTC', back_populates='rooms')
    room = relationship('Room', back_populates='users')

    role = Column(Enum(USER_RTC_ROOM_ROLE), default=0)

    def __init__(self, role):
        self.code = self.__code_prefix__ + uuid.uuid4().hex
        self.role = role
        
class User_RTC(Base):
    """
    model for relating User_Code to RTC data
    Represents a user (Client or firm)    
    """

    __tablename__ = 'user_rtcs'
    __code_prefix__ = 'UR__'

    # Object referencing
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(36), primary_key=False, autoincrement=False, unique=True, nullable=False)
    
    # Modifcation/Creation tracking
    created_datetime = Column(DateTime(timezone=True), default=datetime.utcnow())
    modified_datetime = Column(DateTime(timezone=True), onupdate=datetime.utcnow())
    # Active record
    active = Column(Boolean, index=False, nullable=False, default=True)

    user_code = Column(String(36), index=True, nullable=False, unique=True)

    rooms = relationship('Room', secondary='user_rtc_room_associations')

    user_tokens = relationship('User_Token', back_populates='user')
    
    def __init__(self, user_code):
        self.code = self.__code_prefix__ + uuid.uuid4().hex
        self.user_code = user_code

    def generate_new_code(self):
        self.code = self.__code_prefix__ + uuid.uuid4().hex
        return code


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

    users = relationship('Room', secondary='user_rtc_room_associations')

    def __init__(self, users):
        self.code = self.__code_prefix__ + uuid.uuid4().hex
        for user in users:
            self.users.append(user)

    def generate_new_code(self):
        self.code = self.__code_prefix__ + uuid.uuid4().hex


class User_Token(Base):
    """
    model for relating User_Code to RTC data
    Represents a user (Client or firm)    
    """

    __tablename__ = 'user_tokens'
    __code_prefix__ = 'UT__'

    # Object referencing
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(36), primary_key=False, autoincrement=False, unique=True, nullable=False)
    
    # Modifcation/Creation tracking
    created_datetime = Column(DateTime(timezone=True), default=datetime.utcnow())
    modified_datetime = Column(DateTime(timezone=True), onupdate=datetime.utcnow())
    # Valid record
    valid = Column(Boolean, index=False, nullable=False, default=True)

    user_access_token = Column(String(256), index=True, nullable=False, unique=True)

    
    user_id = Column(Integer, ForeignKey('user_rtcs.id'))
    user = relationship('User_RTC', back_populates='user_tokens')


    def __init__(self, user_code):
        self.code = self.__code_prefix__ + uuid.uuid4().hex
        self.user_code = user_code
        self.user_access_token = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=256))

    def generate_new_code(self):
        self.code = self.__code_prefix__ + uuid.uuid4().hex
        return self.code