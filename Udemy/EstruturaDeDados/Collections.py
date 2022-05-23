from collections import deque

d = deque()

d.append(3) #Adiciona no lado direito
d.appendleft(2) #Adiciona no lado esquerdo
d.append(4)
d.appendleft(1)

for i in d:
    print(i, end = ' ')
print()

d.pop() #Remove da direita
d.popleft() #Remove da esquerda
d.remove(3) #Remove o elemento selecionado

for i in d:
    print(i, end = ' ')
print()