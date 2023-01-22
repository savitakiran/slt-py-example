#!/usr/bin/env python

"""
Author: Nick Russo
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains the value
    of all the sides.
    """
    decimal_places = 2

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """
        Compute the area using the formula √[s(s-a)(s-b)(s-c)]
        where s is the semi-perimeter of the triangle, s=(a+b+c)/2
        """
        s = self.semi_perimeter()
        return round(sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter using the formula sum of all the sides of a triangle
        """
        return (self.a + self.b + self.c) 

    def is_equilateral(self):
        """
        Determine if the triangle is equilateral by comparing the side lengths
        for equality. 
        """
        return self.a == self.b == self.c
    
    def semi_perimeter(self):
        """
        Compute the semi-perimeter using the formula (a+b+c)/2
                """
        return (self.a + self.b + self.c) / 2
