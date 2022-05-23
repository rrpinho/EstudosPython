import random

print(random.randrange(4)) #Número inteiro entre (0, n-1)
print(random.randint(1, 4)) #Número inteiro entre (a, b)

lista = ['Monte', 'castelho', 'pao']
print(random.choice(lista)) #Seleciona um valor aleatorio presente na lista
print(random.sample(lista, 2)) #Retorna uma lista com a quantidade n de valores aleatorios presentes na lista.
print(random.random()) #Número flutuante entre (0, 1(
print(random.uniform(1, 10)) #Número flutuante entre (a, b(
random.shuffle(lista) #Embaralha a sequencia da lista
print(lista)