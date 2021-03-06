from Pass_Go import db_session
from Pass_Go.sql_models import (
    User, )
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, SignUpForm, ResetPasswordForm

User_Blueprint = Blueprint('user', __name__)


@User_Blueprint.route('/', methods=['GET'])
def home():

    context = {
        'None': None,
    }

    return render_template('home.html', **context)


@User_Blueprint.route('/myprofile', methods=['GET'])
@login_required
def myprofile():
    form = ResetPasswordForm()
    return render_template("profile.html", form=form)


@User_Blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # redirect if alread authed
    if current_user.is_authenticated:
        return redirect(url_for('user.myprofile'))

    # Check if post request and if form is filled
    if request.method == 'POST' and form.validate_on_submit():
        user = db_session.query(User).filter_by(email=form.email.data).first()
        # check hash
        if user and user.check_password(form.password.data):
            # create new session
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash("Invalid login details")

    return render_template('login.html', form=form)


@User_Blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    # create signup form
    form = SignUpForm()
    if current_user.is_authenticated:
        return redirect(url_for('user.myprofile'))

    # check if valid creation request and if this email has been used before
    if request.method == 'POST' and form.validate_on_submit() and len(
            db_session.query(User).filter_by(email=form.email.data).all()) < 1:
        new_user = User(email=form.email.data,
                        password=form.password.data,
                        username=form.username.data)
        db_session.add(new_user)
        db_session.commit()
        # create new session
        login_user(new_user)
        return redirect(url_for('user.myprofile'))

    return render_template('signup.html', form=form)


@User_Blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))


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
