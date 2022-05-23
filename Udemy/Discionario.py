d = {}

d['joao'] = 20
d['maria'] = 30
d['pedro'] = 25
print(d)

for k in d.keys():
    print(k + '-' + str(d[k]))

chave_procurada = 'joao'
if chave_procurada in d.keys():
    print('chave encontrada')
else:
    print('Chave NÃO encontrada')

del d['joao'] #Deleta a chave do discionário
if chave_procurada in d.keys():
    print('chave encontrada')
else:
    print('Chave NÃO encontrada')