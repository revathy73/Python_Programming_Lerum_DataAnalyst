"""
You are given the variables a, b, c, which represent the sides of a triangle.
Determine if the triangle is equilateral, isosceles, or scalene

Save your result in a variable called result

Types of triangles
An equilateral triangle is one in which all sides are equal in length.
An isosceles triangle is one in which at least two sides are equal in
length
A scalene triangle is one in which no side is equal in length.
Example Solution
Assume that
a is 30
b is 30
c is 30
Then
result is equilateral
"""

from to_do import TODO


def guide11(a: int, b: int, c: int) -> str:

     if a == b and b == c and c == a:
         result = "equilateral"
     elif a == b or a == c or b ==c:
         result = "isosceles"
     else:
         result = "scalene"

     return result

     """
     # Another Method :: 2 
     if a == b and b == c and c == a:
         return "equilateral"
     elif a == b or a == c or b ==c:
          return "isosceles"   
     else:
         return "scalene" 
                  
     """

