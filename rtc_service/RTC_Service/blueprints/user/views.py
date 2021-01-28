from RTC_Service import db_session
from RTC_Service.sql_models import (
    # TODO import SQLAlchemy Models
)
from flask import Blueprint

User_Blueprint = Blueprint('user', __name__)


@Admin_Blueprint.route('/', methods=['GET'])
def home():
    return 'Home', 200
