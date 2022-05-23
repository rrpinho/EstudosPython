'''
	Tendo uma lista de números inteiros indo de 1 a 15,
imprima esta mesma, porém, sempre que um número seja múltiplo
de 3 a palavra "fizz" deve ser impressa. E quando for
múltiplo de 5, a palavre "buzz" deve ser impressa.
'''
lista = range(1,16)
for i in lista:
	if(i%15 == 0):
		print('fizzbuzz')
	elif(i%5 == 0):
		print('buzz')
	elif(i%3 == 0):
		print('fizz')
	else:
		print(i)