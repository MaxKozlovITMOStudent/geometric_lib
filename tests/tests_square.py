import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    
    def test_area_positive_integers(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(10), 100)
    
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    
    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), 6.25)
        self.assertAlmostEqual(area(1.1), 1.21)
        self.assertAlmostEqual(area(0.5), 0.25)
    
    def test_area_negative(self):
        self.assertEqual(area(-5), 25)
        self.assertEqual(area(-2.5), 6.25)
    
    def test_perimeter_positive_integers(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(10), 40)
    
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)
        self.assertAlmostEqual(perimeter(1.1), 4.4)
    
    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-5), -20)
        self.assertEqual(perimeter(-2.5), -10)
    
    def test_large_numbers(self):
        self.assertEqual(area(1000), 1000000)
        self.assertEqual(perimeter(1000), 4000)
    
    def test_small_numbers(self):
        self.assertAlmostEqual(area(0.001), 0.000001)
        self.assertAlmostEqual(perimeter(0.001), 0.004)
    
    def test_consistency(self):
        result1 = area(5)
        result2 = area(5)
        self.assertEqual(result1, result2)
        self.assertEqual(perimeter(3), perimeter(3))   
    def test_square_as_special_rectangle(self):
        side = 6
        self.assertEqual(area(side), side * side)
        self.assertEqual(perimeter(side), 4 * side)
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