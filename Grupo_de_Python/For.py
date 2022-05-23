for i in range(6):
	print(str(i))
print('\n')
for i in range(2,6):
	print(str(i))
print('\n')
for i in range(6,0,-1):
	print(str(i))

print('\n\n')
print("###############")
print('\n\n')

vetor = ['teste', 'teste1', 'teste2', 'teste3']
for letter in 'aeiouAEIOU':
	print(letter)
print('\n')
for index in vetor:
	print(index)

print('\n\n')
print("###########")
print('\n\n')

lista = range(10)
for index in lista:
	if index == 8:
		print(index)
		break
else:
	print(lista)