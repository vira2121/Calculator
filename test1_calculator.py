import Calculator
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.x=34
        self.y=30
    def tearDown(self):
        self.x=0
        self.y=0

#class TestCalculator(unittest.TestCase):
    def test_add(self):
        x = 10
        y = 20
        result = Calculator.add(x,y)
        self.assertEqual(result, x+y)
    def test_sub(self):
        x = 20
        y = 10
        result = Calculator.sub(x,y)
        self.assertEqual(result, x-y)
    def test_mul(self):
        x = 5
        y = 10
        result = Calculator.mul(x,y)
        self.assertEqual(result, x * y)
    def test_div(self):
        x = 2
        y = 10
        result = Calculator.div(x,y)
        self.assertEqual(result, x/y)

if __name__=="__main__":
    unittest.main()