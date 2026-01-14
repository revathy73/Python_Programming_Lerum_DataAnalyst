import math
from itertools import count


class Student:

    def __init__(self,grades):
        self.grades = grades

    def get_grades(self):
        return self.grades

    def gpa(self):

        if len(self.grades) == 0:
            return 0.0

        total = 0.0
        result = 0.0
        for grade in self.grades:
            total += grade

        result = total / len(self.grades)
        return result

    def bonus(self):

        result = []
        for grade in self.grades:
            new_grade = grade + 1
            result.append(new_grade)
        self.grades = result
        return self.grades

    def lowest(self):
        if len(self.grades) == 0:
            return 0.0

        lowest_grade = math.inf
        for grade in self.grades:
            if grade < lowest_grade:
                lowest_grade = grade

        return lowest_grade

    def highest(self):

        highest_grade = 0.0
        for grade in self.grades:
            if grade > highest_grade:
                highest_grade = grade

        return highest_grade


if __name__ == "__main__":

      john = Student([77.0, 79.0, 88.0, 90.0, 100.0])
      print(john.grades)
      print(john.gpa())
      print(john.lowest())
      print(john.highest())
      print(john.bonus())