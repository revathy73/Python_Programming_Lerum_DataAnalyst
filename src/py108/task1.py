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

