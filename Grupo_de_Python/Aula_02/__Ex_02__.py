'''
	Crie uma função para censurar uma determinada palavra
de uma frase. Sua função deve receber uma string para
frase, uma string para a palavra.
'''

def my_function(frase, palavra):
	tamPalavra = len(palavra)
	subsPalavra = []
	for i in range(tamPalavra):
		subsPalavra.append('*')
	subsPalavraString = ''.join(subsPalavra)
	for palavra in frase:
		my_list = frase.split()
		indice = my_list.index(palavra)
		my_list[indice] = subsPalavraString
		frase = ' '.join(my_list)
	print(frase)
myfrase = input('Digite a frase(Com um palavrao): ')
mypalavra = input('Digite o palavrao que contem na sua frase: ')
my_function(myfrase, mypalavra)