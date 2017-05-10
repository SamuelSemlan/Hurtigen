import os
from peewee import PostgresqlDatabase, Model, CharField
from playhouse.db_url import connect

DATABASE = "hurtigen"
db = PostgresqlDatabase(DATABASE)

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
	db = connect(DATABASE_URL)
else:
	DATABASE = "hurtigen"
	db = PostgresqlDatabase(DATABASE)

class BaseModel(Model):
	class Meta:
		database = db

class Contact(BaseModel):
	email = CharField()	
	message = CharField()

class Password(BaseModel):
	password = CharField()