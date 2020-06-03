from flask import Flask, request, Response
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
    response = Response(unidades(cpf), mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route("/faturas/<uc>/<ano>/<mes>")
#@auth.login_required
def get_fatura(uc, mes, ano):
    response = Response(fatura(uc, mes + '/' + ano), mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/faturas/<uc>")
#@auth.login_required
def get_faturas(uc):
    response = Response(faturas(uc), mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response
