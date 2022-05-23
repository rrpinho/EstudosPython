class Transporte:
    def __init__(self, nome, peso, preco):
        self.nome = nome
        self.peso = peso
        self.preco = preco

    def getNome(self):
        return self.nome
    
    def getPeso(self):
        return self.peso
    
    def getPreco(self):
        return self.preco

t = Transporte('Fusca', 500, 3278.56)
print(t.getNome())
print(t.getPeso())
print(t.getPreco())

class Carro(Transporte):
    def __init__(self, nome, peso, preco, seguro):
        Transporte.__init__(self, nome, peso, preco)
        self.seguro = seguro
    
    def getSeguro(self):
        return self.seguro

carro = Carro('Camaro', 436.24, 82456.58, 2300)
print(carro.getNome())
print(carro.getPeso())
print(carro.getPreco())
print(carro.getSeguro())