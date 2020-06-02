import requests
from bs4 import BeautifulSoup

url = 'http://2via.equatorialalagoas.com.br:8081/segundavia/listafaturas.php'
url2 = 'http://2via.equatorialalagoas.com.br:8081/segundavia/listauc.php'

form = {"uc": "12618390"}
form2 = {"cpf": "09448949413"}
form3 = {"cpf": "42758173468"}

r = requests.post(url2, data=form3)

soup = BeautifulSoup(r.content, 'html.parser')

#print(r)
#print(r.text)

unidades = soup.find_all('td', class_='linha') #soup.find_all('input', {"name": "uc"})

#print(soup.find_all('td', class_='linha'))

for i in range(0, int(len(unidades)/3)):
	print('uc: ', unidades[i*3].strong.text)
	print('end: ', unidades[i*3+1].strong.text)
	
	print('--------------------------')


#print(unidades[2])


#linhas = soup.find_all('td', class_='linha')

#print(len(linhas)/4)

# for i in range(0, int(len(linhas)/4)):
# 	print('mes: ', linhas[i*4].strong.text)
# 	print('venc: ', linhas[i*4+1].strong.text)
# 	print('valor: ', linhas[i*4+2].strong.text)

# 	aberto = None
# 	try:
# 		aberto = linhas[i*4+3].form.input['value']
# 	except:
# 		pass

# 	if aberto: print('status: Em aberto')
# 	else: print('status: Pago')

# 	print('--------------------------')
