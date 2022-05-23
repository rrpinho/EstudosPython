# __ antes de uma variável torna ela privada para a função em que se encontra.
class pessoa:
    def __init__(self):
        self.__nome = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

p = pessoa()
p.nome = 'bat'
print(p.nome)