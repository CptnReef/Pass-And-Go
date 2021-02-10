# from Pass_Go import db_session
# from Pass_Go.sql_models import (
#     # TODO import SQLAlchemy Models
# )
from flask import Blueprint, Flask, request, redirect, render_template, url_for

User_Blueprint = Blueprint('user', __name__)


@User_Blueprint.route('/', methods=['GET'])
def home():

    context = {
        'None': None,
    }
    
    return render_template('home.html', **context)

@User_Blueprint.route('/', methods=['GET', 'POST'])
def create(changename_id):
    if request.method == 'POST':
        pass
    else:
        pass
    pass

@User_Blueprint.route('/', methods=['GET'])
def read(changename_id):
    if request.method == 'POST':
        pass
    else:
        pass
    pass

@User_Blueprint.route('/', methods=['GET', 'POST'])
def update(changename_id):
    if request.method == 'POST':
        pass
    else:
        pass
    pass

@User_Blueprint.route('/', methods=['POST'])
def delete(changename_id):
    pass

