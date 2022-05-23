'''
Faça um programa para uma loja de tintas.
O programa devera pedir o tamanho (em metros^2) da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros^2.
A tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
OBS: Somente são vendidos um número inteiro de latas
'''
area = int (input("Digite a quantidade em metros^2 da área a ser pintada: "))
if area%54 == 0:
    latas = area/54
elif area%54 != 0:
    latas = int(area/54)+1
valor = latas*80
print ("São necessárias %d latas e o custo será %.2f" %(latas,valor))
