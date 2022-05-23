lista = [20, 15, 5, 10]
lista.sort()
print (lista)
lista.sort(reverse=True)
print(lista)

nomes = ['marcos', 'maria', 'carol']
nomes.sort()
print(nomes)
nomes.sort(reverse=True)
print(nomes)

import operator
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade

p1 = Pessoa('Marcos', 28)
p2 = Pessoa('Pedro', 20)
p3 = Pessoa('Carol', 30)
p4 = Pessoa('Yankee', 25)

pessoas = [p1, p2, p3, p4]
pessoas.sort(key=operator.attrgetter('idade'))
for pessoa in pessoas:
    print('Nome %s, idade %d' % (pessoa.getNome(), pessoa.getIdade()))
print()
pessoas.sort(key=operator.attrgetter('idade'), reverse=True)
for pessoa in pessoas:
    print('Nome %s, idade %d' % (pessoa.getNome(), pessoa.getIdade()))