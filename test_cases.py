#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    # 有効同値
    def test_valid_input_min(self):
        self.assertEqual(calc(1, 1), 1)

    def test_valid_input_max(self):
        self.assertEqual(calc(999, 999), 999 * 999)

    def test_valid_input_middle(self):
        self.assertEqual(calc(500, 500), 500 * 500)

    # 無効同値 - 範囲外
    def test_A_below_min(self):
        self.assertEqual(calc(0, 500), -1)

    def test_A_above_max(self):
        self.assertEqual(calc(1000, 500), -1)

    def test_B_below_min(self):
        self.assertEqual(calc(500, 0), -1)

    def test_B_above_max(self):
        self.assertEqual(calc(500, 1000), -1)

    # 無効同値 - 非整数入力
    def test_A_is_float(self):
        self.assertEqual(calc(1.5, 500), -1) 

    def test_B_is_float(self):
        self.assertEqual(calc(500, 2.3), -1)

    def test_A_is_string(self):
        self.assertEqual(calc('a', 500), -1)

    def test_B_is_string(self):
        self.assertEqual(calc(500, "xyz"), -1)

    def test_A_is_special_character(self):
        self.assertEqual(calc("#", 500), -1)

    def test_B_is_special_character(self):
        self.assertEqual(calc(500, "!"), -1)

    def test_A_is_empty(self):
        self.assertEqual(calc("", 500), -1)

    def test_B_is_empty(self):
        self.assertEqual(calc(500, ""), -1) 

    def test_A_is_None(self):
        self.assertEqual(calc(None, 500), -1) 

    def test_B_is_None(self):
        self.assertEqual(calc(500, None), -1) 
