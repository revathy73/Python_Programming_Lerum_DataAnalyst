"""
Create a class called Circle that satisfies the following requirements:

1. The class contains one attribute:

radius of type Double
It cannot be accessed from outside the class
2. A method called area

No parameters
The method can be executed from outside the class
Returns the area of the circle as a Double
3. A method called perimeter

No parameters
The method can be executed from outside the class
Returns the perimeter of the circle as a Double
"""
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        return area

    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return  perimeter

if __name__ == "__main__":

    circle1 = Circle(7)
    print(circle1.area())
    print(circle1.perimeter())
