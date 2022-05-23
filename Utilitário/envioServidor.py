import requests

#res = requests.post('http://sistemaelysiumapi.pythonanywhere.com/api/inserir/dados', json={"token" : "token-8I2B4M7D4P1P9E-maq-waterfarmmaq", "key": "34-65-86/975", "eg": "1", "tm": "04.04.2018-21:49:50", "tp": "22.5", "tb": "4", "nv": "30", "ph": "6", "rs": "boa"})
res = requests.post('http://meupure.com/api/aquaris/enviar/dados/modulo',json={"token": "token-8I2B4M7D4P1P9E-cnt-peixe", "idM": '1', 'tm': '20.06.2018-19:38:32', 'od': '6', 'tp': '22', 'ra': '1', 'ro': '0'})

if res.ok:
    data = res.json()
    print(data)
    print(data['result'])
    print(data['data'])
else:
    print('Erro, json não obtido!')