# -*- encoding: utf-8 -*-

import unittest


class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return True if ((self.x == other.x) and (self.y == other.y)) else False

    def __ne__(self, other):
        return True if ((self.x != other.x) or (self.y != other.y)) else False



class TestPoint(unittest.TestCase):
    def setUp(self):
        self.A = Point(5, 6)
        self.B = Point(6, 10)
        self.C = Point(5.8, 6.8)
        self.D = Point(-5, -6)

    def test_init(self):
        self.assertEqual((self.A.x, self.A.y), (float(5), float(6)), "The abtained values are not real number!!")
        self.assertEqual((self.B.x, self.B.y), (float(6), float(10)), "The abtained values are not real number!!")
        self.assertEqual((self.C.x, self.C.y), (float(5), float(6)), "The abtained values are not real number!!")
        self.assertEqual((self.D.x, self.D.y), (float(-5), float(-6)), "The abtained values are not real number!!")

    def test_str(self):
        self.assertTrue(str(self.A) == "(5.0, 6.0)", "Incorrect output!!!")
        self.assertTrue(str(self.B) == "(6.0, 10.0)", "Incorrect output!!!")
        self.assertTrue(str(self.C) == "(5.0, 6.0)", "Incorrect output!!!")
        self.assertTrue(str(self.D) == "(-5.0, -6.0)", "Incorrect output!!!")

    def test_eq(self):
        self.assertFalse(self.A == self.C,
                        "These two points are equal, but as a result of testing, they turned out to be unequal!")
        self.assertFalse(self.A == self.B,
                        "There two points are unequal, but as a result of testing, they turned out to be equal!")
        self.assertFalse(self.A == self.D,
                        "There two points are unequal, but as a result of testing, they turned out to be equal!")

    def test_ne(self):
        self.assertTrue(self.A != self.C,
                        "These two points are equal, but as a result of testing, they turned out to be unequal!")
        self.assertTrue(self.A != self.B,
                         "There two points are unequal, but as a result of testing, they turned out to be equal!")
        self.assertTrue(self.A != self.D,
                         "There two points are unequal, but as a result of testing, they turned out to be equal!")

if __name__ == '__main__':
    unittest.main()