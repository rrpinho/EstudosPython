'''
	Crie uma função que receberá um número "n" inteiro
como parâmetro e retorne o "n"-zímo termo da sequência
de Fibonacci. Imprima este termo.
'''
def fibonacci(num):
	a=0
	b=1
	cont=1
	c=0
	while (cont <= num):
		c=a+b
		cont+=1
		a=b
		b=c
	return c
num = int(input('Digite o termo procurado: '))
print('O termo ',num,' é: ',fibonacci(num))