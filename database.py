from peewee import SqliteDatabase, Model, CharField

DATABASE = "hurtigen.db"
db = SqliteDatabase(DATABASE, threadlocals=True)

class BaseModel(Model):
	class Meta:
		database = db

class Contact(BaseModel):
	email = CharField()	
	message = CharField()