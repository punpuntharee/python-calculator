import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
      # Add the following test methods to the TestCalculator class:   
        self.assertEqual(self.calc.add(10, -5), 5)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(10,3),7)
        self.assertEqual(self.calc.subtract(-2,-2),0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,4),20)
        self.assertEqual(self.calc.multiply(5,-4),-20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)         
        self.assertEqual(self.calc.divide(-10, -2), 5)      
        self.assertEqual(self.calc.divide(10, -2), -5)     
        self.assertEqual(self.calc.divide(-10, 2), -5)       
        self.assertEqual(self.calc.divide(2, 10), 0)         
        self.assertEqual(self.calc.divide(0, 2), 0)         
        self.assertEqual(self.calc.divide(10, 0), "error")   
        self.assertEqual(self.calc.divide(0, 0), "error")    

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(4,3),1)
        self.assertEqual(self.calc.modulo(-4,3),2)
        self.assertEqual(self.calc.modulo(4,-3),-2)
        self.assertEqual(self.calc.modulo(-4,-3),-1)
        
if __name__ == '__main__':
    unittest.main()