pavimentos = ['inicio', 'Reservatório', 'G1', 'G2', 'G3']
idAtividadeInicialDoProximoPavimento = 0
linhaDeBalanco = []
posicaoX = 0
posicaoY = 0
proximoX = 0
duracaoObra = 0 #ItaloSegundoDia
for pavimento in pavimentos:
    posicaoX = proximoX
    atividadesDoPavimento = [['1','fundação','2', '0'], ['2','estrutura','3', '1'], ['3','alvenaria','1', '0']]
    linhaDeBalanco[posicaoY].append([]) #Pinho que fez, adicionando a 2°dimensão. Duvida se é na posição X ou na Y
    linhaDeBalanco.insert(posicaoY, [])
    for atividade in atividadesDoPavimento:
        idAtividade = atividade[0]
        nome = atividade[1]
        duracao = atividade[2]
        intervalo = atividade[3]
        for x in range(int(duracao)):
            #linhaDeBalanco[posicaoX][posicaoY].append(nome)
            linhaDeBalanco[posicaoY].insert(posicaoX, nome)
            posicaoX += 1
        if(posicaoX > duracaoObra): #ItaloSegundoDia
        	duracaoObra = posicaoX #ItaloSegundoDia
        for x in range(int(intervalo)):
            #linhaDeBalanco[posicaoX][posicaoY].append()
            linhaDeBalanco[posicaoY].insert(posicaoX, None)
            posicaoX +=1    
        if idAtividadeInicialDoProximoPavimento == 0:
            posicaoX = 0
        elif idAtividadeInicialDoProximoPavimento == idAtividade:
            proximoX = posicaoX
    posicaoY += 1
    if pavimento == 'Inicio':
    	idAtividadeInicialDoProximoPavimento = 0
    else:
        idAtividadeInicialDoProximoPavimento = 1
                    
print(linhaDeBalanco)