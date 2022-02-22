from flask import flask
app = flask(__name__)

@app.route('/')
def index():
    return 'Página inicial'



@app.router('/sobre')
def sobre():
    return 'Sobre mim'