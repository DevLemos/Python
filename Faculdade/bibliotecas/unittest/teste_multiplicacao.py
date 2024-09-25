import unittest

def multiply(a, b):
  return a * b

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(5, 10), 50)
        self.assertEqual(multiply(2, 1), 2)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(100, 0), 0)
        self.assertEqual(multiply(2, 2), 4)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)