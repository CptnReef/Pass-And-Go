from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from Pass_Go.models import User
from Pass_Go import db_session


class SignUpForm(FlaskForm):
    """Form for creating a new user"""

    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])

    email = StringField("Email", validators=[DataRequired(), Length(min=3, max=80), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign Up')

    # need User model from db for this to work
    # --
    def validate_email(self, email):
        user = db_session.query(User).filter_by(email=self.email.data).first()
        if user:
            raise ValidationError(
                'That email is already in use by a different account.')


class LoginForm(FlaskForm):
    """Form for logging in a user"""
    email = StringField("Email", validators=[DataRequired(), Length(min=3, max=80), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
