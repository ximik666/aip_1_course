# Тесты и отладка
import unittest

def average(a):
    return sum(a) / len(a) if a else None

class AverageTests(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(average([]))
    def test_values(self):
        self.assertAlmostEqual(average([1, 2]), 1.5)

assert average([1, 2]) == 1.5
