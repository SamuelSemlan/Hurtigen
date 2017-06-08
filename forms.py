from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, validators



class MyForm(FlaskForm):
	name = StringField("Name", [validators.InputRequired()])
	message = TextAreaField("Message", [validators.InputRequired()])

class LoginForm(FlaskForm):
	password = PasswordField("Password", [validators.InputRequired()])