# from Pass_Go import db_session
# from Pass_Go.sql_models import (
#     # TODO import SQLAlchemy Models
# )
from flask import Blueprint, request, render_template
from .forms import LoginForm, SignUpForm

User_Blueprint = Blueprint('user', __name__)


@User_Blueprint.route('/', methods=['GET'])
def home():

    context = {
        'None': None,
    }

    return render_template('home.html', **context)


@User_Blueprint.route('/login', methods=['GET'])
def login():
    # create login form
    form = LoginForm()

    return render_template('login.html', form=form)


@User_Blueprint.route('/signup', methods=['GET'])
def signup():
    # create signup form
    form = SignUpForm()

    return render_template('signup.html', form=form)


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
