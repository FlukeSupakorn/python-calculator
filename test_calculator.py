import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(100, 200), 300) 
        self.assertEqual(self.calc.add(-50, -25), -75) 

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1000, 500), 500) 
        self.assertEqual(self.calc.subtract(-20, -10), -10) 

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(-5, -4), 20) 

    def test_divide(self):
        self.assertEqual(self.calc.divide(100, 25), 4)  
        self.assertEqual(self.calc.divide(-20, -5), 4)  

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(100, 7), 2) 
        self.assertEqual(self.calc.modulo(15, 4), 3) 

if __name__ == '__main__':
    unittest.main()