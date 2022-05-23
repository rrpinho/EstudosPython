'''array1=[] #Array vazio
array =[7, 2.34, "Rafa"] #Array pode ter vários tipos
array1.append("Posição") #Adicionando a string ao array1
'''
'''#Calcule a media de 5 notas usando Arrays
notas=[1,2,3,4,5]
cont,i=0,0
while i<5:
    cont=cont+notas[i]
    i+=1
print("A média foi %.2f" %(cont/i))
'''
'''
#Faça um programa que leia um vetor de 5 números inteiros e mostre o vetor
vetor = []
i=1
while i<=5:
    n=int(input("Digite um número: "))
    vetor.append(n)
    i+=1
print("Vetor lido: ", vetor)
'''
#Faça um programa que leia algumas notas e mostre as notas e a média na tela
notas = []
Qnotas = int(input("Quantas notas serão digitadas: "))
soma,x=0,Qnotas
while x >0:
    nota=(float(input("Digite uma nota: ")))
    soma=soma+nota
    notas.append(nota)
    x-=1
print("As notas digitadas foras: ", notas)
print("A média foi: %.2f" %(soma/Qnotas))
