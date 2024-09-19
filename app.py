from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!111!!</p>"

@app.route("/user/")
@app.route("/user/<name>")
def hello(name=None):
    return render_template('hello.html', person=name)
