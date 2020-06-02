import requests
from bs4 import BeautifulSoup

from base import Session, engine, Base

from Unidade import Unidade


url = 'http://2via.equatorialalagoas.com.br:8081/segundavia/listauc.php'
form = {"cpf": "42758173468"}

response = requests.post(url, data=form)

soup = BeautifulSoup(response.content, 'html.parser')

unidades = soup.find_all('td', class_='linha')

dict_uc = {}

Base.metadata.create_all(engine)
session = Session()

for i in range(0, int(len(unidades)/3)):
	try:
		session.add(Unidade(unidades[i*3].strong.text, unidades[i*3+1].strong.text))
	except:
		print('Não foi possível inserir a UC ', unidades[i*3].strong.text)
	dict_uc[unidades[i*3].strong.text] = unidades[i*3+1].strong.text


session.commit()
session.close()

print(dict_uc)