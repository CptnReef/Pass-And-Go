from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
# from Pass_Go.models import User


class SignUpForm(FlaskForm):
    """Form for creating a new user"""
    username = StringField('User Name',
                           validators=[DataRequired(),
                                       Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    # need User model from db for this to work
    # --
    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError(
    #             'That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    """Form for logging in a user"""
    username = StringField('User Name',
                           validators=[DataRequired(),
                                       Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
