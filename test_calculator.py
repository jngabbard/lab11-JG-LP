import unittest
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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()