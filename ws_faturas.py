import requests
import json
from bs4 import BeautifulSoup

def faturas(uc):
	url = 'http://2via.equatorialalagoas.com.br:8081/segundavia/listafaturas.php'
	form = {"uc": uc} # "12618390"

	response = requests.post(url, data=form)

	soup = BeautifulSoup(response.content, 'html.parser')

	linhas = soup.find_all('td', class_='linha')
	faturas = []

	for i in range(0, int(len(linhas)/4)):
		mes = (linhas[i*4].strong.text)
		vencimento = (linhas[i*4+1].strong.text)
		valor = (linhas[i*4+2].strong.text)

		aberto = None
		status = 'Pago'
		try:
			aberto = linhas[i*4+3].form.input['value']
			status = 'Em aberto'
		except:
			pass

		dados = {}
		dados['uc'] = uc
		dados['status'] = status
		dados['mes'] = mes
		dados['vencimento'] = vencimento
		dados['valor'] = valor
		

		faturas.append(dados)


	return json.dumps(faturas)


#print(json.dumps(faturas("12618390")))