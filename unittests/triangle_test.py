"""
Author: Nick Russo
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.a8b11c13 = Triangle(8, 11, 13)
        self.a5b5c5 = Triangle(5, 5, 5)
        self.a4b6c8 = Triangle(4, 6, 8)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.a8b11c13.area(), 43.82)
        self.assertEqual(self.a5b5c5.area(), 10.83)
        self.assertEqual(self.a4b6c8.area(), 11.62)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.a8b11c13.perimeter(), 32)
        self.assertEqual(self.a5b5c5.perimeter(), 15)
        self.assertEqual(self.a4b6c8.perimeter(), 18)

    def test_semi_perimeter(self):
        """
        Compare the test rectangle perimeter computations to the actual values.
        """
        self.assertEqual(self.a8b11c13.semi_perimeter(), 16)
        self.assertEqual(self.a5b5c5.semi_perimeter(), 7.5)
        self.assertEqual(self.a4b6c8.semi_perimeter(), 9)


    def test_is_equilateral(self):
        """
        Confirm or deny if the triangle is equilateral.
        """
        self.assertFalse(self.a8b11c13.is_equilateral())
        self.assertTrue(self.a5b5c5.is_equilateral())
        self.assertFalse(self.a4b6c8.is_equilateral())
