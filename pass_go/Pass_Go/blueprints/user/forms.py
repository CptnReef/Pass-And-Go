from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from Pass_Go.sql_models import User


class SignUpForm(FlaskForm):
    """Form for creating a new user"""

    username = StringField('User Name',
                           validators=[DataRequired(),
                                       Length(min=3, max=50)])

    email = StringField(
        "Email", validators=[DataRequired(),
                             Length(min=3, max=80),
                             Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already in use by a different account.')


class LoginForm(FlaskForm):
    """Form for logging in a user"""
    email = StringField(
        "Email", validators=[DataRequired(),
                             Length(min=3, max=80),
                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class ResetPasswordForm(FlaskForm):
    """For resetting a user's password"""
    oldPassword = PasswordField('Old Password', validators=[DataRequired()])
    newPassword = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')
