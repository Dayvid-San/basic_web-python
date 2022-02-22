from flask import flask, render_template
app = flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



@app.router('/sobre_mim')
def sobre():
    return render_template("about.html")


# "Nome" é o nome da variavel
@app.router('/<string:nome')
def error404(nome):
    variavel = f'Página ({nome}) não existe'
    return render_template("error.html", vaviavel=variavel)