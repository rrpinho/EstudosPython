'''
    3) Defina uma função para que, recebendo uma lista de números, retorne a média destes.
    Depois, defina funções para retornar a mediana, o maior número e o menor número.
'''
def funcao(numeros):
    media = 0.0
    tam = len(numeros)
    for i in numeros:
        media += i
    return media/tam
def mediana(numeros):
    tam = len(numeros)
    if(tam%2 != 0):
        return tam/2
    else:
       return ((tam/2)+((tam/2)-1))/2
def maior(numeros):
    numero = 0
    for i in numeros:
        if(numero<i):
            numero=i
    return numero
    #numero.sort()
    #return numero[(len(numeros))-1]
def menor(numeros):
    numero = 0
    for i in numeros:
        if(numero>i):
            numero=i
    return numero
    #numeros.sort()
    #return numeros[0]
