import requests
import json
from bs4 import BeautifulSoup

def unidades(cpf):
	url = 'http://2via.equatorialalagoas.com.br:8081/segundavia/listauc.php'
	form = {"cpf": cpf}

	response = requests.post(url, data=form)

	soup = BeautifulSoup(response.content, 'html.parser')

	unidades = soup.find_all('td', class_='linha')

	list_uc = []

	for i in range(0, int(len(unidades)/3)):
		dict_uc = {}
		
		dict_uc['uc'] = unidades[i*3].strong.text
		dict_uc['endereco'] = unidades[i*3+1].strong.text

		list_uc.append(dict_uc)


	return (json.dumps(list_uc))