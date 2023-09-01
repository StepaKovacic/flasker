from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    first_name = "John"
    stuff = "This is Bold text"


    pizza = ["peperoni", "cheeze", 41, True]
    return render_template("index.html", 
        first_name=first_name,
        stuff=stuff,
        pizza=pizza )

@app.route("/user/<name>")
def user(name):
	return render_template("user.html", name=name)


@app.route("/simon/spinava/noha")
def simon():
	return "Simon spinava noha"

#create custo error page

#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500