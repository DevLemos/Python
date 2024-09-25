import unittest

#Definindo uma função para testar
def soma(a,b):
    return a + b

#Criando uma classe de teste:
class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(3,4),7)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)