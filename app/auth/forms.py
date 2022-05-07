from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    initials = StringField("Initials", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    initials = StringField("Initials", validators=[DataRequired()])
    nickname = StringField("Nickname", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_initials(self, initials):
        user = User.query.filter_by(initials=initials.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")
