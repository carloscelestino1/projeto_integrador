def consult_cnpj(cnpj):
    cnpj_= cnpj
    
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj_}"
    querystring = {f"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj":"06990590000123", "plugin":"RF"}
    response = requests.request('GET', url, params=querystring)

    resp = json.loads(response.text)
    print(response)

    return(resp)

consult_cnpj(49190159000105)