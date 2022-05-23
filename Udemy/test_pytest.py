#Arquivo de teste tem quem ser nomeado: test_*
#A função que irá testar tem que estar nomeada como test_*()

def fatorial(n):
    if (n == 0):
        return 1
    return n * fatorial(n - 1)

def test_fatorial():
    assert fatorial(0) == 1

def ehPar(n):
    if n % 2 == 0:
        return True
    return False

def test_ehPar():
    assert ehPar(10) == True