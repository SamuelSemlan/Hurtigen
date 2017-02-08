from flask import Flask, render_template

app = Flask("hurtigen")

@app.route("/")
def home():
	return render_template("home.html")


@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/profile/")
def profile():
	return render_template("profile.html")

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)

