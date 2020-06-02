from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from web_scraper import unidades, faturas, fatura

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route("/")
#@auth.login_required
def hello():
    return "Hello, World!"

@app.route("/unidades")
#@auth.login_required
def get_unidades():
    cpf = request.args.get('cpf')
    return unidades(cpf)

@app.route("/faturas/<uc>/<mes_ano>")
#@auth.login_required
def get_fatura(uc, mes_ano):
    mes_ano = mes_ano.replace('_', '/')
    return fatura(uc, mes_ano)

@app.route("/faturas/<uc>")
#@auth.login_required
def get_faturas(uc):
    return faturas(uc)
