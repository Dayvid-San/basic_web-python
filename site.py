from flask import flask, render_template, request
from random import randint
app = flask(__name__)

@app.route('/', methods=["GET, POST"])
def index():
    variavel = "Game: Adivinhe o número correto (de 0 à 9)"

    if request.method =="GET":
        return render_template("index.html", variavel=variavel)
    else:
        numero = randint(0,9)
        palpite = int(request.form.get("name"))
        if numero == palpite:
            return '<h1>Resultado: Você ganhou</h1>'
        else:
            return '<h1>Você perdeu</h1>'





@app.router('/sobre_mim')
def sobre():
    return render_template("about.html")


# "Nome" é o nome da variavel
@app.router('/<string:nome')
def error404(nome):
    variavel = f'Página ({nome}) não existe'
    return render_template("error.html", vaviavel=variavel)