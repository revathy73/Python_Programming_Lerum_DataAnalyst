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
