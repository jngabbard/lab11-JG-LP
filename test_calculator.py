# https://github.com/jngabbard/lab11-JG-LP
# Partner 1: Joshua Gabbard
# Partner 2: Leslie Paulsen

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert add(1, 1) == 2
        assert add(5, -2) == 3
        assert add(0, 5) == 5

    def test_subtract(self): # 3 assertions
        assert subtract(2, 1) == 1
        assert subtract(5, -4) == 9
        assert subtract(5, 0) == 5
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-2,4), -8)
        self.assertEqual(mul(0,50), 0)



    def test_divide(self): # 3 assertions
        self.assertEqual(div(12,3),4)
        self.assertEqual(div(4,-2),-2)
        self.assertEqual(div(100,10),10)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(4, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(2, 16), 4)
        self.assertEqual(log(5,1), 0)


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
            log(1, 8)
        with self.assertRaises(ValueError):
            log(1, 0)
        with self.assertRaises(ValueError):
            log(3, -2)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(0),0)
        self.assertEqual(square_root(81),9)
        with self.assertRaises(ValueError):
            square_root(-10)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()