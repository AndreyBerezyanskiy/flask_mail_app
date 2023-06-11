from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class EmailForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    email = EmailField("Email", [DataRequired()])
    submit = SubmitField("Login")
