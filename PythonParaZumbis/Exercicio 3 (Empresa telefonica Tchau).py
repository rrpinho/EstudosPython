#Considere a empresa de teleonia Tchau.
#Calcule a conta de telefone do cliente baseado nos minutos de uso
#200min ou menos a empresa cobra R$0.20 por minuto
#Entre 200 e 400 minutos a empresa cobra R$0.18 por minuto
#Acima de 400 minutos a empresa cobra R$0.15 por minuto

minutos = int(input("Minutos utilizado: "))
if minutos<200:
      preço=0.20
elif minutos<=400:
      preço=0.18
elif minutos<=800:
      preço=0.15
else:
      preço=0.08
print("Conta telefônica: R$%6.2f" %(minutos*preço))


'''
print ("#######Bem-Vindo a empresa Tchau#######")
print("Digite quantos tempo você usou seu telefone. (Em minutos)")
minutos = int(input(""))
if minutos<200:
      conta = minutos*0.20
elif minutos>=200 and minutos<400:
      conta = minutos*0.18
elif minutos>=400:
      conta = minutos*0.15
elif minutos >=800:
      conta = minutos*0.08
print ("Sua conta ficou no valor de: R$%.2f" %conta)
'''
