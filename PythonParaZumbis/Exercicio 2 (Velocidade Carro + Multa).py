print("Qual a velocidade do carro? Obs: Número inteiro e em Km/h")
velocidade = int (input("Digite a velocidade do carro: "))
if velocidade > 110:
    multa = (velocidade - 110) * 5
    print("Você foi multado no valor de R$%.2f" %multa)
else:
    print("Parabéns, você está dirigindo à uma velocidade permitida")
