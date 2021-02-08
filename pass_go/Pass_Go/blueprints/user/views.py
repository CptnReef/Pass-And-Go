# from Pass_Go import db_session
# from Pass_Go.sql_models import (
#     # TODO import SQLAlchemy Models
# )
from flask import Blueprint

User_Blueprint = Blueprint('user', __name__)


@User_Blueprint.route('/', methods=['GET'])
def home():
    return 'Home'

