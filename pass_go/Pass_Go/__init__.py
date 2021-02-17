import os, json
from flask import Flask, send_from_directory
from sqlalchemy import create_engine
from Pass_Go.config import Config
import datetime
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager

config = Config.get_instance()

app = Flask(__name__, static_folder="static")

app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['RTC_SERVICE_URL'] = config.RTC_SERVICE_URL
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from Pass_Go.sql_models import (User, Base)

#### SQLALCHEMY SETUP ####
db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
# create metadata
Base.metadata.create_all(db_engine)
# create session
Session = sessionmaker(bind=db_engine)
db_session = Session()
db_session.commit()

#### AUTH ####
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_code):
    return db_session.query(User).filter_by(code=user_code).first()


#### ADD ROUTING ####

from Pass_Go.blueprints.user.routes import User_Blueprint
from Pass_Go.blueprints.main.routes import Main_Blueprint

app.register_blueprint(User_Blueprint, url_prefix='/')
app.register_blueprint(Main_Blueprint, url_prefix='/')


@app.after_request
def after_request(response):
    return response


@app.route("/favicon.ico")
def favicon():
    """Sends the favicon to the client"""
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "./favicon.ico")
