import unittest

from Stuff70 import *


class TestBubbleSort(unittest.TestCase):
    def test_Simple(self):
        input_val = [7, 3, 4, 1, 59, 84, 37, 7347, 839, 9, 2, 0]
        expected_input = [0, 1, 2, 3, 4, 7, 9, 37, 59, 84, 839, 7347]
        calculated = bubble(input_val)
        self.assertEqual(expected_input, calculated)

    def test_Negative(self):
        input_val = [-1,-2,-10, 2, 21, 69, 420,-7347, 7347]
        expected_input = [-7347, -10, -2, -1, 2, 21, 69, 420, 7347]
        calculated = bubble(input_val)
        self.assertEqual(expected_input, calculated)

if __name__ == "__main__":
    unittest.main()