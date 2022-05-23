class Conta(object):
	def __init__(self, nome, valor):
		self.nome = nome
		self.valor = valor

class ContaPoupanca(object):
	def __init__(self, nome, valor, taxaCrescimento):
		super(ContaPoupanca, self).__init__(nome, valor)
		self.taxaCrescimento = taxaCrescimento

class ContaCorrente(object):
	def __init__(self, nome, valor, taxaCrescimento, taxaManutencao):
		super(ContaCorrente, self).__init__(nome,valor,taxaCrescimento)
		self. taxaManutencao = taxaManutencao