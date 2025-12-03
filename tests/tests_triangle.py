import unittest
import math
from triangle import area
from triangle import perimeter
class TestTriangle(unittest.TestCase):
    def test_area_intenger_numbers(self):
        self.assertEqual(area(10, 5), 25)
        self.assertEqual(area(4, 6), 12)
        self.assertEqual(area(7, 3), 10.5)
    
    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_float(self):
        self.assertAlmostEqual(area(3.5, 2.0), 3.5)
        self.assertAlmostEqual(area(2.2, 4.4), 4.84)
    
    def test_area_negative(self):
        self.assertEqual(area(-5, 4), -10)
        self.assertEqual(area(5, -4), -10)
        self.assertEqual(area(-5, -4), 10)
    
    def test_perimeter_three_sides(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)
        self.assertEqual(perimeter(2, 3, 4), 9)
    
    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(0, 0, 5), 5)
        self.assertEqual(perimeter(0, 0, 0), 0)
    
    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.5), 10.5)
        self.assertAlmostEqual(perimeter(1.1, 2.2, 3.3), 6.6)
    
    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-3, 4, 5), 6)
        self.assertEqual(perimeter(-3, -4, 5), -2)
        self.assertEqual(perimeter(-3, -4, -5), -12)

    def test_large_numbers(self):
        self.assertEqual(area(1000, 500), 250000)
        self.assertEqual(perimeter(100, 200, 300), 600)
        
    def test_minimal_positive(self):
        self.assertAlmostEqual(area(0.001, 0.001), 0.0000005)
        self.assertAlmostEqual(perimeter(0.001, 0.001, 0.001), 0.003)
    
    def test_consistency(self):
        result1 = area(5, 4)
        result2 = area(5, 4)
        self.assertEqual(result1, result2)
        self.assertEqual(perimeter(3, 4, 5), perimeter(3, 4, 5))
    
    def test_perimeter_symmetry(self):
        self.assertEqual(perimeter(3, 4, 5), perimeter(4, 3, 5))
        self.assertEqual(perimeter(3, 4, 5), perimeter(5, 4, 3))
        self.assertEqual(perimeter(3, 4, 5), perimeter(3, 5, 4))

if __name__ == "__main__":
    unittest.main()