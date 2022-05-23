#Calule a soma de números inteiros até ser digitado zero
soma = 0
while True:
    x=int(input("Digite o número (0->Sai): "))
    if x==0:
        break
    soma=soma+x
print("A soma foi: %d" %soma)
