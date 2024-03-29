# OneMax Problem with Simulated Annealing
import random, math
class OneMax:
    def __init__(self, size):
        self.size = size
        self.solution = [random.randint(0,1) for i in range(size)]
        self.cost = self.obj_fun(self.solution)

    #Gerar um vizinho
    def neighbor(self):
        new_neighbor = self.solution[:]
        pos = random.randint(0, self.size - 1)
        new_neighbor[pos] = 1 if new_neighbor[pos] == 0 else 0
        return new_neighbor

    #Função objetivo, retorna a qualidade
    def obj_fun(self, solution):
        return sum(solution)

    '''
        Simulated Annealing
        T -> Temperatura Inicial
        T_min -> Temperatura Mínimo
        Alpha -> Decaimento da emperatura
        max_iter -> Quantidade de iterações com uma mesma temperatura
    '''
    def run_anneal(self, T = 1.0, T_min = 0.00001, alpha = 0.9, max_iter = 100):
        while T > T_min:
            #Iterações com uma mesma temperatura
            for i in range (max_iter):
                new_solution = self.neighbor() #Gera uma nova solução
                new_cost = self.obj_fun(new_solution) #Calcula o custo dessa nova solução
                delta = self.cost - new_cost #Calcula a diferença dos custos
                ap = math.exp(-delta / T) #Probabilidade de aceitação de uma solução de piora

                if ap > random.random(): #Verifica se aceita ou não
                    self.solution = new_solution[:] #Copia a nova solução
                    self.cost = new_cost #Atribui o novo custo

            T = T * alpha

    def get_solution(self):
        return self.solution

one_max = OneMax(20)
print('Solução inicial: %s' % str(one_max.get_solution()))
one_max.run_anneal()
print('Solução final: %s' % str(one_max.get_solution()))