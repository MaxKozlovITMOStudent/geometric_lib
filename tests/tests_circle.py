import unittest
import math
from circle import area, perimeter 

class TestCircle(unittest.TestCase):
    
    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), 4 * math.pi)
    
    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)
    
    def test_area_float_radius(self):
        self.assertAlmostEqual(area(2.5), math.pi * 2.5 * 2.5)
    
    def test_area_negative_radius(self):
        self.assertAlmostEqual(area(-1), math.pi)
    
    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)
    
    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)
    
    def test_perimeter_negative_radius(self):
        self.assertAlmostEqual(perimeter(-1), -2 * math.pi)
    
    def test_performance_area(self):
        import time
        start = time.time()
        for _ in range(10000):
            area(5)
        end = time.time()
        self.assertLess(end - start, 0.1)
    
    def test_performance_perimeter(self):
        import time
        start = time.time()
        for _ in range(10000):
            perimeter(5)
        end = time.time()
        self.assertLess(end - start, 0.1)
if __name__ == "__main__":
    unittest.main()