import unittest
import math
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    
    def test_area_zero_value(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_positive_numbers(self):
        self.assertEqual(area(5, 4), 20)
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(area(1, 100), 100)
        self.assertEqual(area(100, 1), 100)
    
    def test_area_float_numbers(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(area(3.7, 2.1), 7.77)
        self.assertAlmostEqual(area(0.5, 0.5), 0.25)
    
    def test_area_large_numbers(self):
        self.assertEqual(area(1000, 500), 500000)
        self.assertEqual(area(10**6, 10**6), 10**12)
    
    def test_area_negative_numbers(self):
        self.assertEqual(area(-5, 4), -20)
        self.assertEqual(area(5, -4), -20)
        self.assertEqual(area(-5, -4), 20)
    
    def test_perimeter_negative_numbers(self):
        self.assertEqual(perimeter(-5, 4), -2)
        self.assertEqual(perimeter(5, -4), 2)
        self.assertEqual(perimeter(-5, -4), -18)
    
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 7), 20)
        self.assertEqual(perimeter(5, 5), 20)
        self.assertEqual(perimeter(1, 1), 4)
        self.assertEqual(perimeter(10, 20), 60)
    
    def test_perimeter_float_numbers(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0)
        self.assertAlmostEqual(perimeter(1.1, 2.2), 6.6)

    def test_small_values(self):
        self.assertAlmostEqual(area(0.0001, 0.0001), 0.00000001)
        self.assertAlmostEqual(area(999.999, 999.999), 999998.000001)
    
    def test_commutative_property(self):
        a, b = 7, 3
        self.assertEqual(area(a, b), area(b, a))
        self.assertEqual(perimeter(a, b), perimeter(b, a))
    
    def test_time(self):
        import time
        start = time.time()
        for i in range(10000):
            area(5, 4)
        end = time.time()
        self.assertLess(end - start, 0.1)

if __name__ == "__main__":
    unittest.main()