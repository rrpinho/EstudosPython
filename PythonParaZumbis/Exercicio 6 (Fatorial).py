'''#Calcule o fatorial de 10
n=10
fatorial=1
while n>=1:
    fatorial=fatorial*n
    n= n-1
print ("O fatorial é %.2f"%fatorial)'''
'''i=1
fat = 1
while i<=10:
    fat = fat*i
    i=i+1
print("Fat(10) = %d" %fat)'''
#Calcular o fatorial de um número digitado
fatorial = 1
n = int(input("Digite o número que deseja o fatorial: "))
j=n
while n>=1:
    fatorial=fatorial*n
    n=n-1
print("O fatorial %d é: %d" %(j,fatorial))
