'''
    4) Defina uma lista que receberá os horários de um cinema fictício. Preencha esta lista com filmes à sua escolha,
    em forma de dicionário. Obrigatoriamente, os campos que o dicionários devem ter são: horário, 3D, nome, sala e
    preço. Outros campos podem ser adicionados. O mínimo de filmes na lista é 5.

    5) Com relacão ao exercício 4, crie um método para venda de ingressos para seus filmes. O dicionário do ingresso
    deve ter os campos de nome do usuário, nome do filme, sala, horário.

    6) Com relacão ao exercício 4, crie um método de busca. Os parâmetros devem ser o nome do filme e se ele é 3D.
    Retorne uma mensagem de erro caso o filme não esteja na lista. Caso contrário, retorne o nome do filme, junto com
    sua sala/horário.
'''
def ingresso(filme):
    usuario = input('Digite seu nome: ')
    ingressos = {'Usuário': usuario, 'Filme': filme}
    print(ingressos)

def busca(sessoes):
    filme = input('Digite o nome do filme: ')
    d = input('O filme é em 3D? ')
    for i in sessoes:
        if ((filme == i['Nome']) and (d == i['3D'])):
            return i
    else:
        print('Filme não encontrado.')

nome = ['001', '002', '003', '004', '005']
horario = ['07:00', '10:00', '13:00', '16:00', '19:00']
d = ['sim', 'nao', 'sim', 'nao', 'sim']
sala = ['100', '200', '300', '400', '500']
preco = ['0.00', '1.00', '2.00', '3.00', '4.00']
sessoes = []
for i in range(5):
    sessoes.append({
        'Nome': nome[i],
        'Horario': horario[i],
        '3D': d[i],
        'Sala': sala[i],
        'Preco': preco[i]
    })
ingresso(sessoes[0])
#print(busca(sessoes))