import requests
from bs4 import BeautifulSoup

def get_fatura(uc, mes_ano):
	url = 'http://2via.equatorialalagoas.com.br:8081/segundavia/fatura.php'
	form = {"uc": uc, "fd": "0", "mes_ano": mes_ano}

	response = requests.post(url, data=form)

	soup = BeautifulSoup(response.content, 'html.parser')

	dados = soup.find_all('td')
	
	dict_boleto = {'NF': dados[5].text[4:], 'nome': dados[6].text, 'logradouro': dados[7].text, 'bairro': dados[8].text,
	               'cep': dados[9].text.split()[0], 'cidade': dados[9].text.split()[1], 'uf': dados[10].text,
	               'uc': dados[15].text, 'mes': dados[16].text, 'periodo': dados[17].text, 'consumo': dados[21].text,
	               'vencimento': dados[22].text, 'total': dados[23].text, 'cod_barras': dados[39].text }

	return dict_boleto

#print(get_fatura('12618390', "05/2020"))