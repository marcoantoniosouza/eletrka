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

def faturas(uc):
    url = 'http://2via.equatorialalagoas.com.br:8081/segundavia/listafaturas.php'
    form = {"uc": uc} # "12618390"

    response = requests.post(url, data=form)

    soup = BeautifulSoup(response.content, 'html.parser')

    linhas = soup.find_all('td', class_='linha')
    faturas = []

    for i in range(0, int(len(linhas)/4)):
        mes_ano = (linhas[i*4].strong.text)
        mes, ano = mes_ano.split('/')

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
        dados['ano'] = ano
        dados['vencimento'] = vencimento
        dados['valor'] = valor
        

        faturas.append(dados)


    return json.dumps(faturas)

def fatura(uc, mes_ano):
    url = 'http://2via.equatorialalagoas.com.br:8081/segundavia/fatura.php'
    form = {"uc": uc, "fd": "0", "mes_ano": mes_ano}

    response = requests.post(url, data=form)

    soup = BeautifulSoup(response.content, 'html.parser')

    dados = soup.find_all('td')
    dict_fatura = {}
    try:
        dict_fatura = {'NF': dados[5].text[4:], 'nome': dados[6].text, 'logradouro': dados[7].text, 'bairro': dados[8].text,
                       'cep': dados[9].text.split()[0], 'cidade': dados[9].text.split()[1], 'uf': dados[10].text,
                       'uc': dados[15].text, 'mes': dados[16].text, 'periodo': dados[17].text, 'consumo': dados[21].text,
                       'vencimento': dados[22].text, 'total': dados[23].text, 'cod_barras': dados[39].text }
    except:
        pass

    return json.dumps(dict_fatura)