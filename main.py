from flask import Flask, request, render_template

app = Flask(__name__)  # need!! double underscore


# Routing / mapping. Tying URL to python function. Always need a return statement

@app.route('/')  # Homepage with '/'
def index():
    return "This is the Homepage"


@app.route('/shopping/<name>')
def shopping(name):
    food = ["Jalepenos", "Habeneros", "Go-gurt", "Sugar"]
    return render_template("shopping.html", food=food, name=name)


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":  # Only start web server when this file is called directly
    app.run(debug=True)  # starts app
