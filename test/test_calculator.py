from unittest import TestCase

from src.calculator import calculator_check


class Test(TestCase):
    def test_add_calculator_check(self):
        try:
            self.assertEqual(calculator_check("+", 1, 2), 3)
        except AssertionError:
            print("FAILED test_add_calculator_check: 1+2 was not 3")

    def test_sub_calculator_check(self):
        try:
            self.assertEqual(calculator_check("-", 1, 2), -1)
        except AssertionError:
            print("FAILED test_sub_calculator_check: 1+2 was not -1")

    def test_mult_calculator_check(self):
        try:
            self.assertEqual(calculator_check("*", 1, 2), 2)
        except AssertionError:
            print("FAILED test_mult_calculator_check: 1*2 was not 2")

    def test_div_calculator_check(self):
        try:
            self.assertEqual(calculator_check("/", 1, 1), 1)
        except AssertionError:
            print("FAILED test_div_calculator_check: 1/1 was not 1")

    def test_mod_calculator_check(self):
        try:
            self.assertEqual(calculator_check("%", 1, 1), 0)
        except AssertionError:
            print("FAILED test_mod_calculator_check: 1%1 was not 0")


"""
Main starts here
"""
if __name__ == '__main__':
    Test.main()
