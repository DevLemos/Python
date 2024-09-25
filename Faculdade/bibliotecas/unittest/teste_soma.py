import unittest

def soma(a,b):
    return a + b

class TestSoma(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(soma(3, 4), 7)
    
    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(0, 5), 5)
        self.assertEqual(soma(0, -3), -3)

if __name__ == '__main__':
    unittest.main()