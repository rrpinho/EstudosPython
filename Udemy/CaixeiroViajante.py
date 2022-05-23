import random, time, sys

class geradorGrafo:
    
    def __init__(self, n):
        self.n = n
        self.grafo = [[] for i in range(n)]
        self.custos = {}

    def gerar_grafo(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if (i, j) and (j, i) not in self.custos:
                        custo = random.randint(1, 100)
                        self.custos[(i, j)] = custo
                        self.custos[(j, i)] = custo
                    self.grafo[i].append(j)

    def mostrar_grafo(self):
        for i in range(self.n):
            print('Adjacentes de %d:' % i, end = ' ')
            for adj in self.grafo[i]:
                print('$%d -> %d' % (self.custos[i, adj], adj), end = ' ')
            print('')

# PROBLEMA DO CAIXEIRO VIAJANTE
    #Método Random
    def pcv_random(self, iteracoes):
        melhor_cirtuito = []
        melhor_custo = None
    
        def gerar_circuito(melhor_cirtuito, melhor_custo):
            vertices = [i for i in range(1, self.n)]
            circuito = [0]
            custo_circuito = 0

            while len(vertices) > 0:
                e = random.choice(vertices)
                vertices.remove(e)
                custo_circuito += self.custos[(circuito[-1], e)]
                circuito.append(e)

            custo_circuito += self.custos [(circuito[-1], 0)]

            if melhor_custo is None:
                melhor_cirtuito = circuito[:]
                melhor_custo = custo_circuito
                print('Circuito Inicial: %s - Custo: %d' % (str(melhor_cirtuito), melhor_custo))
            
            else:
                if custo_circuito < melhor_custo:
                    melhor_cirtuito = circuito[:]
                    melhor_custo = custo_circuito
            
            return(melhor_cirtuito, melhor_custo)

        for i in range(iteracoes):
            melhor_cirtuito, melhor_custo = gerar_circuito(melhor_cirtuito, melhor_custo)
            #print('Iter %d: Melhor circuito: %s - Custo: %d' % (i + 1, str(melhor_cirtuito), melhor_custo))
            #time.sleep(1)
        print('Melhor circuito: %s - Custo: %d' % (str(melhor_cirtuito), melhor_custo))
    
    #Método Genetico
    def pcv_genetico(self, tam_pop, geracoes, tam_torneio, prob_cruz):
        pop = [] #População

        def gerar_individuo():
    
            vertices = [i for i in range(1, self.n)]
            individuo = [0]

            while len(vertices) > 0:
                e = random.choice(vertices)
                vertices.remove(e)
                individuo.append(e)
            return individuo

        #Função de Fitness (Avaliação quão boa é a solução)
        def obter_custo(individuo):
            custo = 0
            for i in range(self.n - 1):
                custo += self.custos[(individuo[i], individuo[i + 1])]
            custo += self.custos[(individuo[-1], individuo[0])]
            return custo

        #Gerando a população Inicial
        for i in range (tam_pop):
            pop.append(gerar_individuo())

        #A cada Geração
        for i in range(geracoes):
            #Seleção por torneio
            for j in range(tam_torneio):
                if random.random() <= prob_cruz:
                    pai1, pai2 = None, None
                    while True:
                        pai1 = random.randint(0, tam_pop - 1)
                        pai2 = random.randint(0, tam_pop - 1)
                        if pai1 != pai2:
                            break
                    
                    #Cruzamento de um ponto
                    while True:
                        #Selecioando um ponto.
                        ponto = random.randint(0, self.n - 1)
                        
                        if ponto != 0 and ponto != (self.n - 1):
                            gen1_validos = [i for i in range(self.n)]
                            gen2_validos = gen1_validos[:]
                            gen1, gen2 = [], []
                            
                            for p in range(ponto):

                                if pop[pai1][p] not in gen1:
                                    gen1.append(pop[pai1][p])
                                    gen1_validos.remove(pop[pai1][p])
                                else:
                                    e = random.choice(gen1_validos)
                                    gen1.append(e)
                                    gen1_validos.remove(e)

                                if pop[pai2][p] not in gen2:
                                    gen2.append(pop[pai2][p])
                                    gen2_validos.remove(pop[pai2][p])
                                else:
                                    e = random.choice(gen2_validos)
                                    gen2.append(e)
                                    gen2_validos.remove(e)

                            for p in range(ponto, self.n):

                                if pop[pai2][p] not in gen1:
                                    gen1.append(pop[pai2][p])
                                    gen1_validos.remove(pop[pai2][p])
                                else:
                                    e = random.choice(gen1_validos)
                                    gen1.append(e)
                                    gen1_validos.remove(e)

                                if pop[pai1][p] not in gen2:
                                    gen2.append(pop[pai1][p])
                                    gen2_validos.remove(pop[pai1][p])
                                else:
                                    e = random.choice(gen2_validos)
                                    gen2.append(e)
                                    gen2_validos.remove(e)
                            
                            sys.exit(1)
                            break

grafo = geradorGrafo(10)
grafo.gerar_grafo()
#grafo.pcv_random(10000)
grafo.pcv_genetico(tam_pop = 10, geracoes = 100, tam_torneio = 2, prob_cruz = 1)