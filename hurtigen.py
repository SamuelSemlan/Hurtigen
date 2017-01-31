from flask import Flask, render_template

app = Flask("hurtigen")
name = "Semlan"
visits = 0

@app.route("/")
def home():
	return render_template("home.html")


@app.route("/about/")
def about():
	return render_template("test.html")

if __name__ == "__main__":
	app.run(debug=True)

