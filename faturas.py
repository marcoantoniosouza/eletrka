import json

import requests
from bs4 import BeautifulSoup

from base import Session, engine, Base

from Fatura import Fatura
import boleto

def get_faturas(uc):
	url = 'http://2via.equatorialalagoas.com.br:8081/segundavia/listafaturas.php'
	form = {"uc": uc} # "12618390"

	response = requests.post(url, data=form)

	soup = BeautifulSoup(response.content, 'html.parser')

	linhas = soup.find_all('td', class_='linha')
	faturas = []

	Base.metadata.create_all(engine)
	session = Session()

	for i in range(0, int(len(linhas)/4)):
		
		aberto = None
		status = 'Pago'
		try:
			aberto = linhas[i*4+3].form.input['value']
			status = 'Em aberto'
		except:
			pass

		dados = None
		dados = boleto.get_fatura(uc, linhas[i*4].strong.text)
		dados['status'] = status

		faturas.append(dados)

		total = str(dados['total'][3:]).replace('.', '').replace(',', '.')

		fat = Fatura(dados['uc'], dados['mes'], dados['periodo'],
			         float(total), dados['vencimento'], dados['cod_barras'],
			         dados['consumo'])

		try:
			session.add(fat)
		except:
			pass

	session.commit()
	session.close()

	return faturas


print(json.dumps(get_faturas("12618390")))