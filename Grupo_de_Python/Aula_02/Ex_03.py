'''
	Simule uma tabela de preços de uma feira usando
dicionário. Crie uma função recebendo como parâmetro a
lista de compras de uma cliente e o dicionário. A função
deve retornar o preço total das compras da cliente.
'''

def funcao(menu, compras):
	preco = 0.0
	listKeys = menu.keys()
	for key in listKeys:
		for i in compras:
			if(key == i):
				preco += menu[key]
	return (preco)

menu = {
	'Batata': 1.20, 
	'Cenoura': 0.80, 
	'Aipim': 5.50, 
	'Tomate': 2.30
}
compras = ['Batata', 'Cenoura']
print('O valor a pagar é:',(funcao(menu, compras)))