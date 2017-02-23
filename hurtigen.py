from flask import Flask, render_template, request

app = Flask("hurtigen")


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        page = "{} + {} = {}".format(
            request.form["first_number"],
            request.form["second_number"],
            int(request.form["first_number"]) + int(request.form["second_number"])
            )
        return page
    else:
        return render_template("contact.html")

@app.route("/profile")
def profile():
	return render_template("profile.html")

@app.route("/settings")
def settings():
	return render_template("settings.html")


if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)

