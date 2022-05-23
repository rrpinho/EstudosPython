'''
	Crie um dicionário com keys sendo relacionados à
inteiros. Crie uma função cujos parâmetros sejam uma
string e o seu dicionário. Na string, a aparição das
keys deve ser substituida pelo número que se relaciona
à key em questão. Retorne a string modificada.
'''

def funcao(string, dicionario):
	string2 = ''
	lista = string.split()
	tamLista = len(lista)
	listaKeys = dicionario.keys()
	for key in listaKeys:
		for i in lista:
			if ( key == i ):
				indice = lista.index(i)
				lista[indice] = dicionario[key]
	for j in range(tamLista):
		string2 += str(lista[j])
	return (string2)

dicionario = {'a':1, 'd':4}
string = 'a b c d'
print('A frase modificada fica: ',(funcao(string, dicionario)))