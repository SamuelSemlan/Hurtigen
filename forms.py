from flask_wtf import FlaskForm
from wtforms import StringField, validators	

class MyForm(FlaskForm):
	name = StringField("Name", [validators.InputRequired()])
	