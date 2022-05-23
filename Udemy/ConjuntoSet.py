c1 = {1,2,3}
c2 = {'marcos', 'maria', 'yankee'}
c3 = {1, 'marcos', 3.14}
c4 = set([1,2,2,3,3,4])

print(type(c1))
print(c4)
print(len(c2))
if 'marcos' in c3:
    print('Elemento encontrado')

c5 = {3, 4, 5, 6}

print(c4 | c5) #União
print(c4 & c5) #Intersecção
print(c5 - c4) #Diferença
print(c4 - c5) #Diferença

c6 = {10,20,30,40}
c6.remove(40)
print(c6)