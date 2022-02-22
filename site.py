from flask import flask, render_template
app = flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



@app.router('/sobre_mim')
def sobre():
    return render_template("about.html")