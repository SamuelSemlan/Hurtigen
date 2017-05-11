from flask import Flask, render_template, request, session, make_response
from forms import MyForm
from forms import LoginForm
from database import db
import os

app = Flask("hurtigen")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "insecure dev key")

@app.before_request
def before_request():
	db.connect()

@app.after_request
def after_request(response):
	db.close()
	return response

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/hemliga/sida")
def track_cookie():
	visit = int(request.cookies.get("visit", 0))
	if visit == 0:
		text = "This is your first visit!"
		resp = make_response(text)
		resp.set_cookie("visit", str(1))
		return resp
	else:
		return "Welcome back!"

@app.route("/secret_page", methods=["POST", "GET"])
def secret_page():
	logged_in = str(session.get("logged_in", "0"))
	form = LoginForm()
	if request.method == "POST":
		if request.form["password"] == "test":
			session["logged_in"] = "1"
			return "Correct!"
		return render_template("secret_page.html", form=form)
	else:
		if logged_in == "1":
			return "This is my secret page!"
		else:
			return render_template("secret_page.html", form=form)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = MyForm()
    if form.validate_on_submit():
        return "Thanks for submitting, {}!".format(form.name.data)
    else:
        return render_template("contact.html", form=form)

@app.route("/profile")
def profile():
	return render_template("profile.html")



@app.route("/settings")
def settings():
	return render_template("settings.html")


if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)

