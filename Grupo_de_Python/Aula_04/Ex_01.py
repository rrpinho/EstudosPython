class Complex(object):
	
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.modulo = float(
			(self.a**2 + self.b**2)**0.5)

	def module(self):
		return self.modulo

	def __repr__(self):
		return '<Complex>:'+str(self.a)+'+'+str(self.b)+'i'

	def __str__(self):
		return str(self.a)+'+'+str(self.b)+'i'
inst = Complex(2,3)
print(inst)