import unittest

def fat(n):
    if (n == 0):
        return 1
    return n * fat(n - 1)

def pot(base, exp):
    if(exp == 0):
        return 1
    return base * pot(base, exp - 1)

class TesteMathMethods(unittest.TestCase):
    def testPot(self):
        self.assertEqual(1024, pot(2, 10))
    
    def testFat(self):
        self.assertEqual(24, fat(4))

unittest.main()