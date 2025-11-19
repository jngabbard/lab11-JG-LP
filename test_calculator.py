# https://github.com/jngabbard/lab11-JG-LP
# Partner 1: Joshua Gabbard
# Partner 2: Leslie Paulsen

import unittest
import calculator
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert add(1, 1) == 2
        assert add(5, -2) == 3
        assert add(0, 5) == 5

    def test_subtract(self): # 3 assertions
        assert sub(2, 1) == 1
        assert sub(5, -4) == 9
        assert sub(5, 0) == 5
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
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(4, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(100, 10), 2)
        self.assertEqual(log(16, 2), 4)
        self.assertEqual(log(1,5), 0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(10, 1)
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
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(8, 15), 17.0)

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