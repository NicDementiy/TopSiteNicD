from flask import Flask, render_template

app = Flask("hi")

@app.route("/")
def hello():
    return "<p>hi, hello</p>"





@app.route("/калькулятор")
def calc():
    return render_template("JS.html")
