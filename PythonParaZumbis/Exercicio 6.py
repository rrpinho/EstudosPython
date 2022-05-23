#Faça um programa que imprima de 1 ate um número digitado peço usuário
'''x=int(input("Digite um valor: "))
y=1
while y<=x:
    print(y)
    y+=1'''
#Imprimir os números pares entre 0 e um número fornecido
'''x=int(input("Digite um número: "))
y=0
while y<=x:
    if y%2 == 0:
        print(y)
    y+=1'''
#Imprimir os números pares entre 0 e um número fornecido (Sem usar "if")
'''a=int(input("Digite um número: "))
x=0
while x<=a:
    while x%2 == 0:
        print (x)
        x+=1
    while x%2 !=0:
        x+=1'''
'''fim = int(input("Digite um número: "))
x=0
while x<=fim:
    print(x)
    x+=2'''
#Faça um programa que imprima apenas os 10 primeiros múltiplis de 3 de uma sequencia de números impares
x=int(input("Digite um número: "))
y=0
while y<=x:
    if y%2 != 0:
        print(y*3)
    y+=1
