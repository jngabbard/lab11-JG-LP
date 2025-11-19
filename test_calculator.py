# https://github.com/jngabbard/lab11-JG-LP
# Partner 1: Joshua Gabbard
# Partner 2: Leslie Paulsen

import unittest
import calculator
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(2,3), 6)
        self.assertEqual(calculator.mul(-2,4), -8)
        self.assertEqual(calculator.mul(0,50), 0)



    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.div(3,12),4)
        self.assertEqual(calculator.div(-2,4),-2)
        self.assertEqual(calculator.div(10,100),10)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            calculator.log(1, 8)
        with self.assertRaises(ValueError):
            calculator.log(1, 0)
        with self.assertRaises(ValueError):
            calculator.log(3, -2)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(),)
        self.assertAlmostEqual(calculator.hypotenuse(),)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(calculator.square_root(0),0)
        self.assertEqual(calculator.square_root(81),9)
        with self.assertRaises(ValueError):
            calculator.square_root(-10)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()