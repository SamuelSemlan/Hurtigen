from flask import Flask, render_template, request

app = Flask("hurtigen")


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        page = "You are {} with the email {} and your message was {}".format(
            request.form["name"],
            request.form["email"],
            request.form["message"]
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

