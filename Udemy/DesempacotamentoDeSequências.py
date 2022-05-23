#Sequência == lista, tupla, string...

lista = [1, 2, 3, 4]

a, _, _, b = lista

print(a)
print(b)
############################################################
def func(x, y = 3): #y=3 é um parametro opicional, ou seja se não passar ele vai assumir esse valor
    return x**2, y**2

print(func(2, 3)) #Recebe uma tupla

r1, r2 = func(4, 5)
print(r1)
print(r2)

