"""
Create a class called Rectangle that satisfies the following requirements:

1. The class has two attributes:

An attribute called base of type Double
An attribute called height of type Double
None of the attributes can be accessed from outside the class
The initial values of the attributes are provided through the constructor

2. A method called perimeter

No parameters
The method can be executed from outside the class
Returns the perimeter of the rectangle as a Double

3. A method called area

No parameters
The method can be executed from outside the class
Returns the area of the rectangle as a Double
Hints
area = base * height

perimeter = 2 * (base + height)
"""
class Rectangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def perimeter(self) -> float:

        perimeter = 2 * (self.base + self.height)
        return perimeter

    def area(self) -> float:

        area = self.base * self.height
        return area


if __name__ == "__main__":

    rec1 = Rectangle(base = 5, height = 7)
    rec2 = Rectangle(base = 7, height = 9)

    print(rec1.perimeter())
    print(rec2.area)

