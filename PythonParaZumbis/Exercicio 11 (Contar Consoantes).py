'''
    Faça um programa que leia um vetor de 10 caracteres minúsculos
    e diga quantas consoantes foram lidas.
'''
vetor = []
Qchar=int(input("Quantos caracteres serão digitados: "))
x,i=0,0
while Qchar >0:
    n=(input("Digite o char: "))
    vetor.append(str(n))
    if n=="a" or n=='e' or n=='i' or n=='o' or n=='u':
        x=x
    else:
        x+=1
    Qchar-=1
print("Foram digitadas %d consoantes" %x)
