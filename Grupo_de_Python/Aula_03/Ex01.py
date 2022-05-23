'''
    1) Crie uma função que instancie uma lista contendo todas as cartas de um baralho comum tendo 4 naipes e 52 cartas
    ao total. Deve-se utilizar métodos de repetiçao. O código deve imprimir cada uma das cartas para o output.
'''
def create_deck():
    naipes = ['Espadas', 'Ouros', 'Copas', 'Paus']
    numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = []
    for naipe in naipes:
        for numero in numeros:
            carta = {'Naipe': naipe, "Valor": numero}
            baralho.append(carta)
    for carta in baralho:
        print('Naipe: %s. Valor: %s' %(carta['Naipe'], carta['Valor']))
    return baralho

'''
    2)
'''
'''def search_card(naipe,valor,baralho):
    for carta in baralho:
        if(carta['Naipe'] == naipe) and (carta['Valor'] == valor):
'''
def error_treat():
    pass

my_deck = create_deck()