from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators	

class MyForm(FlaskForm):
	name = StringField("Name", [validators.InputRequired()])
	message = TextAreaField("Message", [validators.InputRequired()])