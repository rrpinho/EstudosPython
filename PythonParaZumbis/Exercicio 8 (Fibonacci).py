'''A sequência de Fibonacci é a seguinte:
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
    Sua regra de formação é simples: os dois primeiros elementos são 1;
    a partir de então, cada elemento é a soma dos dois anteriores.

    Faça um algoritmo que leia um número inteiro e calcule o seu número
    de Fibonacci. F(1)=1, F(2)=1, F(3)=2, F(4)=3, etc.'''
'''x,y,n=1,1,3
Fibonacci = int(input("Digite uma posição do Fibonacci: "))
while n<=Fibonacci:
    i=0
    i=x+y
    x=y
    y=i
    n=n+1
print("O valor na posição %d foi: %d" %(Fibonacci,i))'''
n=int(input("N: "))
a,b=1,1
k=1
while k<=n-2:
    a,b=b,a+b
    k=k+1
print("Fibonacci(%d) = %d" %(n,b))
