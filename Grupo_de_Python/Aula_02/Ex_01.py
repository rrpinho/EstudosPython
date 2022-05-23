'''
	Crie uma função que receba uma string e uma letra. Esta
função deve retornar o número de vezes que essa letra se
repete na string. Não use o método .count inicialmente.
Depois, recrie a sua função usando count().
'''
def semCount(string, letra):
	cont=0
	string=string.lower()
	letra=letra.lower()
	for i in string:
		if(i == letra):
			cont+=1
	return cont
def comCount(string, letra):
	string=string.lower()
	letra=letra.lower()
	cont = string.count(letra)
	return cont
string = input('Digite a string: ')
letra = input('Digite a letra: ')
print('A letra:"',letra,'"aparece ',semCount(string, letra),' vezes')
print('\n')
print('A letra:"',letra,'"aparece ',comCount(string, letra),' vezes')