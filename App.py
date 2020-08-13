from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from waitress import serve
from web_scraper import unidades, faturas, fatura

app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()

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

if __name__ == "__main__":
   #app.run() ##Replaced with below code to run it using waitress 
   serve(app, host='0.0.0.0', port=5000)