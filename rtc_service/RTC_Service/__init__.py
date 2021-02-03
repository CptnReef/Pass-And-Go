import os, json
from flask import Flask
from sqlalchemy import create_engine
from RTC_Service.config import Config
import datetime
from sqlalchemy.orm import sessionmaker
from flask_socketio import SocketIO

config = Config.get_instance()

app = Flask(__name__, static_folder="static")

app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from RTC_Service.sql_models import (
    User_RTC_Room_Association,
    User_RTC,
    Room,
    User_Token,
    Base
)

#### SQLALCHEMY SETUP ####
db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
# create metadata
Base.metadata.create_all(db_engine)
# create session
Session = sessionmaker(bind=db_engine)
db_session = Session()
db_session.commit()

#### ADD ROUTING ####
# from RTC_Service.blueprints.user.views import User_Blueprint

# app.register_blueprint(User_Blueprint, url_prefix='/')



socketio = SocketIO(app, cors_allowed_origins="*")
import RTC_Service.signaler.events

# @app.after_request
# def after_request(response):    
#     return response

