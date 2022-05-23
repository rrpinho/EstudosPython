'''
	Faça um algoritmo para receber um numero do usuario e 
	retornar se este numero é par ou impar.
'''
num = int(input('Digite um numero: '))
if (num%2 == 0):
	print('O numero: '+str(num)+'  é par.')
else:
	print('O numero: '+str(num)+' é impar.')