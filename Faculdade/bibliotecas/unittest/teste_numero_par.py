import unittest

def eh_par(n):
    return n % 2 == 0

class TesteEhPar(unittest.TestCase):

    def test_numeros_pares(self):
        self.assertTrue(eh_par(2))
        self.assertTrue(eh_par(10))
        self.assertTrue(eh_par(0))
    
    def test_numeros_impares(self):
        self.assertFalse(eh_par(3))
        self.assertFalse(eh_par(7))
        self.assertFalse(eh_par(11))

    def test_numeros_negativos(self):
        self.assertTrue(eh_par(-4))
        self.assertFalse(eh_par(-5))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)